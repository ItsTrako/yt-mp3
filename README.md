<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=7c3aed&height=200&section=header&text=yt-mp3&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Self-hosted%20YouTube%20%E2%86%92%20MP3%20downloader&descAlignY=58&descSize=18&descColor=c4b5fd" width="100%"/>
</div>

<div align="center">

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-7c3aed?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-6d28d9?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-8b5cf6?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![ffmpeg](https://img.shields.io/badge/ffmpeg-required-a78bfa?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-c4b5fd?style=for-the-badge)](LICENSE)

<br/>

> **No cloud. No accounts. No limits.**
> Download audio from any YouTube video directly to your machine.

<br/>

**[🇬🇧 English](#-english) · [🇪🇸 Español](#-español)**

<br/>

</div>

---

## 🇬🇧 English

<br/>

### ✦ What is this?

A fully **local** web app that downloads audio from any YouTube video and converts it to MP3 — all running on your own machine. No APIs, no third-party services, no size limits.

Built with **Python + Flask** on the backend and a single dark-themed HTML file as the frontend. No npm, no build step, no dependencies beyond `pip install`.

<br/>

### ✦ Features

<br/>

<div align="center">

| | Feature | Details |
|:---:|---|---|
| 🎧 | **MP3 download** | Any public YouTube video or short |
| 🔊 | **Quality selector** | 128 / 192 / 320 kbps |
| 📊 | **Live progress bar** | Real-time download + conversion tracking |
| 📁 | **Built-in library** | Browse and re-download past files |
| 🌐 | **Bilingual UI** | Switch between English and Spanish in one click |
| 🌑 | **Dark purple UI** | Clean, local-first interface |
| ⚡ | **Zero build step** | No npm, no webpack, no nonsense |

</div>

<br/>

### ✦ Prerequisites

You need two things installed before running this:

- **Python 3.10+** → [python.org/downloads](https://www.python.org/downloads/)
- **ffmpeg** → used to convert audio to MP3

**Install ffmpeg:**

<div align="center">

| Platform | Command |
|:---:|---|
| 🪟 Windows | `winget install ffmpeg` |
| 🍎 macOS | `brew install ffmpeg` |
| 🐧 Linux | `sudo apt install ffmpeg` |

</div>

Verify: `ffmpeg -version`

<br/>

### ✦ Installation

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/yt-mp3.git
cd yt-mp3

# (Recommended) virtual environment
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# Install
pip install -r requirements.txt

# Run
python app.py
```

Open **[http://localhost:8000](http://localhost:8000)** — done.

<br/>

### ✦ How to use

```
1  →  Paste a YouTube URL
2  →  Pick quality  ( 128 / 192 / 320 kbps )
3  →  Hit  "Download audio"
4  →  Watch the progress bar
5  →  Click the green button to save the MP3
6  →  Find all past downloads in the Library section
```

Files are saved to the `downloads/` folder inside the project.

<br/>

### ✦ Project structure

```
yt-mp3/
├─ app.py              ← Flask server · manages jobs, serves files
├─ requirements.txt    ← Python deps (flask, yt-dlp)
├─ downloads/          ← MP3 output folder (auto-created)
└─ static/
   └─ index.html       ← Entire frontend · one file · no build
```

<br/>

### ✦ How it works

```
Browser  →  POST /api/download  →  Flask spawns thread
                                       ↓
                                   yt-dlp fetches audio
                                       ↓
                                   ffmpeg converts → .mp3
                                       ↓
Browser  ←  GET /api/status     ←  progress polling
Browser  ←  GET /api/file       ←  file download
```

<br/>

> [!WARNING]
> **Local use only.** This app has no authentication or rate limiting.
> Do not expose it on a public server.
> Only download content you have the right to download.

<br/>

---

## 🇪🇸 Español

<br/>

### ✦ ¿Qué es esto?

Una app web completamente **local** para descargar audio de cualquier vídeo de YouTube y convertirlo a MP3 — todo corriendo en tu propia máquina. Sin APIs, sin servicios externos, sin límites de tamaño.

Backend en **Python + Flask**, frontend en un único HTML con tema oscuro. Sin npm, sin build step, solo `pip install`.

<br/>

### ✦ Características

<br/>

<div align="center">

| | Función | Detalle |
|:---:|---|---|
| 🎧 | **Descarga MP3** | Cualquier vídeo o short público de YouTube |
| 🔊 | **Selector de calidad** | 128 / 192 / 320 kbps |
| 📊 | **Barra de progreso en vivo** | Seguimiento en tiempo real de descarga y conversión |
| 📁 | **Biblioteca integrada** | Consulta y vuelve a bajar archivos anteriores |
| 🌐 | **Interfaz bilingüe** | Cambia entre inglés y español con un clic |
| 🌑 | **UI oscura en morado** | Interfaz limpia y local |
| ⚡ | **Sin build** | Sin npm, sin webpack, sin complicaciones |

</div>

<br/>

### ✦ Requisitos

Necesitas dos cosas instaladas:

- **Python 3.10+** → [python.org/downloads](https://www.python.org/downloads/)
- **ffmpeg** → convierte el audio a MP3

**Instalar ffmpeg:**

<div align="center">

| Sistema | Comando |
|:---:|---|
| 🪟 Windows | `winget install ffmpeg` |
| 🍎 macOS | `brew install ffmpeg` |
| 🐧 Linux | `sudo apt install ffmpeg` |

</div>

Verifica: `ffmpeg -version`

<br/>

### ✦ Instalación

```bash
# Clonar
git clone https://github.com/TU_USUARIO/yt-mp3.git
cd yt-mp3

# (Recomendado) entorno virtual
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# Instalar
pip install -r requirements.txt

# Arrancar
python app.py
```

Abre **[http://localhost:8000](http://localhost:8000)** — listo.

<br/>

### ✦ Cómo usar

```
1  →  Pega una URL de YouTube
2  →  Elige la calidad  ( 128 / 192 / 320 kbps )
3  →  Pulsa  "Descargar audio"
4  →  Mira la barra de progreso
5  →  Pulsa el botón verde para guardar el MP3
6  →  Todas las descargas anteriores están en la sección Biblioteca
```

Los archivos se guardan en la carpeta `downloads/` dentro del proyecto.

<br/>

### ✦ Estructura

```
yt-mp3/
├─ app.py              ← Servidor Flask · gestiona trabajos y sirve archivos
├─ requirements.txt    ← Dependencias Python (flask, yt-dlp)
├─ downloads/          ← Carpeta de salida MP3 (se crea automáticamente)
└─ static/
   └─ index.html       ← Frontend completo · un archivo · sin build
```

<br/>

> [!WARNING]
> **Solo uso local.** Esta app no tiene autenticación ni rate limiting.
> No la expongas en un servidor público.
> Descarga únicamente contenido que tengas derecho a descargar.

<br/>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=7c3aed&height=100&section=footer" width="100%"/>

<sub>Made with 🟣 in Spain · MIT License</sub>

</div>
