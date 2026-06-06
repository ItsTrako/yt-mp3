"""
Local YouTube -> MP3 downloader
Backend en Flask que usa yt-dlp + ffmpeg.

USO LOCAL EXCLUSIVAMENTE. No lo pongas en un servidor publico:
no tiene autenticacion ni rate limiting.
"""

import os
import re
import threading
import uuid
from pathlib import Path

from flask import Flask, request, jsonify, send_from_directory, render_template

import yt_dlp

# ---------------------------------------------------------------------------
# Configuracion
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).parent
DOWNLOAD_DIR = BASE_DIR / "downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)

app = Flask(__name__, static_folder="static", template_folder="static")

# Estado de los trabajos en memoria: { job_id: {status, progress, title, filename, error} }
JOBS = {}


# ---------------------------------------------------------------------------
# Validacion basica de URL de YouTube
# ---------------------------------------------------------------------------

YT_REGEX = re.compile(
    r"(https?://)?(www\.)?(youtube\.com/(watch\?v=|shorts/|playlist\?list=)|youtu\.be/)"
)


def is_youtube_url(url: str) -> bool:
    return bool(YT_REGEX.search(url or ""))


def safe_filename(name: str) -> str:
    """Limpia caracteres problematicos del nombre de archivo."""
    return re.sub(r'[\\/*?:"<>|]', "_", name).strip()


# ---------------------------------------------------------------------------
# Logica de descarga (corre en un hilo aparte para no bloquear)
# ---------------------------------------------------------------------------

def make_progress_hook(job_id):
    def hook(d):
        job = JOBS.get(job_id, {})
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
            done = d.get("downloaded_bytes", 0)
            pct = (done / total * 100) if total else 0
            job["progress"] = round(pct, 1)
            job["status"] = "downloading"
        elif d["status"] == "finished":
            job["progress"] = 100
            job["status"] = "converting"  # ffmpeg post-procesa a mp3 aqui
        JOBS[job_id] = job

    return hook


def download_job(job_id, url, quality):
    try:
        outtmpl = str(DOWNLOAD_DIR / "%(title)s.%(ext)s")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": outtmpl,
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "progress_hooks": [make_progress_hook(job_id)],
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": quality,  # 128 / 192 / 320
                }
            ],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "audio")

        # yt-dlp renombra a .mp3 tras el post-procesado
        mp3_name = safe_filename(title) + ".mp3"
        # buscamos el archivo real generado (el titulo puede tener caracteres distintos)
        candidates = sorted(
            DOWNLOAD_DIR.glob("*.mp3"), key=lambda p: p.stat().st_mtime, reverse=True
        )
        if candidates:
            mp3_name = candidates[0].name

        JOBS[job_id].update(
            {"status": "done", "progress": 100, "title": title, "filename": mp3_name}
        )
    except Exception as e:  # noqa: BLE001
        JOBS[job_id].update({"status": "error", "error": str(e)})


# ---------------------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/download", methods=["POST"])
def api_download():
    data = request.get_json(silent=True) or {}
    url = (data.get("url") or "").strip()
    quality = str(data.get("quality") or "192")

    if not is_youtube_url(url):
        return jsonify({"error": "URL de YouTube no valida."}), 400
    if quality not in {"128", "192", "320"}:
        quality = "192"

    job_id = uuid.uuid4().hex
    JOBS[job_id] = {"status": "queued", "progress": 0}

    t = threading.Thread(target=download_job, args=(job_id, url, quality), daemon=True)
    t.start()

    return jsonify({"job_id": job_id})


@app.route("/api/status/<job_id>")
def api_status(job_id):
    job = JOBS.get(job_id)
    if not job:
        return jsonify({"error": "job desconocido"}), 404
    return jsonify(job)


@app.route("/api/file/<path:filename>")
def api_file(filename):
    # as_attachment=True fuerza la descarga en el navegador
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)


@app.route("/api/library")
def api_library():
    files = []
    for p in sorted(DOWNLOAD_DIR.glob("*.mp3"), key=lambda x: x.stat().st_mtime, reverse=True):
        files.append(
            {"name": p.name, "size_mb": round(p.stat().st_size / 1_048_576, 2)}
        )
    return jsonify(files)


if __name__ == "__main__":
    print("\n  YouTube -> MP3 local downloader")
    print("  Abre http://localhost:8000 en tu navegador\n")
    app.run(host="127.0.0.1", port=8000, debug=False)
