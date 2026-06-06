<div align="center">



\# 🎵 yt-mp3



\*\*Self-hosted YouTube to MP3 downloader — no cloud, no accounts, no limits.\*\*



!\[Python](https://img.shields.io/badge/Python-3.10+-8b5cf6?style=flat-square\&logo=python\&logoColor=white)

!\[Flask](https://img.shields.io/badge/Flask-3.0-7c3aed?style=flat-square\&logo=flask\&logoColor=white)

!\[yt-dlp](https://img.shields.io/badge/yt--dlp-latest-6d28d9?style=flat-square)

!\[License](https://img.shields.io/badge/license-MIT-a78bfa?style=flat-square)



\*Built in Spain 🇪🇸 — README available in \[English](#english) and \[Español](#español)\*



</div>



\---



<a name="english"></a>

\## 🇬🇧 English



\### What is this?



A fully local web app to download audio from any YouTube video and save it as an MP3 directly on your machine. No third-party services, no API keys, no upload limits — everything runs on your own computer.



Built with \*\*Flask\*\* (Python backend), \*\*yt-dlp\*\* (YouTube audio extraction) and \*\*ffmpeg\*\* (MP3 conversion). The UI is a single dark-themed HTML file with real-time progress tracking.



\### Features



\- 🎧 Download any YouTube video as MP3

\- 🔊 Choose quality: 128 / 192 / 320 kbps

\- 📊 Real-time progress bar while downloading

\- 📁 Built-in library — browse and re-download past files

\- 🌑 Dark purple UI — looks good, runs local

\- ⚡ No frameworks, no npm, no build step



\### Prerequisites



\- \*\*Python 3.10+\*\* → \[python.org](https://www.python.org/downloads/)

\- \*\*ffmpeg\*\* installed and on your PATH



Install ffmpeg:



| OS | Command |

|---|---|

| Windows | `winget install ffmpeg` |

| macOS | `brew install ffmpeg` |

| Linux | `sudo apt install ffmpeg` |



Verify it works: `ffmpeg -version`



\### Installation



```bash

\# 1. Clone the repo

git clone https://github.com/YOUR\_USERNAME/yt-mp3.git

cd yt-mp3



\# 2. (Optional but recommended) create a virtual environment

python -m venv venv

\# Windows

venv\\Scripts\\activate

\# macOS / Linux

source venv/bin/activate



\# 3. Install dependencies

pip install -r requirements.txt



\# 4. Run

python app.py

```



Then open \*\*http://localhost:8000\*\* in your browser. That's it.



\### Usage



1\. Paste a YouTube URL into the input field

2\. Select audio quality (192 kbps recommended for most uses)

3\. Hit \*\*Descargar audio\*\*

4\. Watch the progress bar — it will tell you when it's downloading vs converting

5\. Click the green button to save the MP3 to your device

6\. All your past downloads are listed in the \*\*Biblioteca\*\* section below



MP3 files are saved to the `downloads/` folder inside the project.



\### Project structure



```

yt-mp3/

├─ app.py              # Flask server — handles download jobs \& serves files

├─ requirements.txt    # Python dependencies

├─ downloads/          # Where MP3s are saved (auto-created)

└─ static/

&#x20;  └─ index.html       # Entire frontend — one file, no build step

```



\### ⚠️ Important



This app is designed for \*\*local use only\*\*. It has no authentication, no rate limiting, and no security hardening. Do not expose it on a public server.



Only download content you have the right to download.



\---



<a name="español"></a>

\## 🇪🇸 Español



\### ¿Qué es esto?



Una app web completamente local para descargar el audio de cualquier vídeo de YouTube y guardarlo como MP3 directamente en tu máquina. Sin servicios externos, sin claves de API, sin límites de subida — todo corre en tu propio ordenador.



Hecho con \*\*Flask\*\* (backend Python), \*\*yt-dlp\*\* (extracción de audio de YouTube) y \*\*ffmpeg\*\* (conversión a MP3). La interfaz es un único archivo HTML con tema oscuro y seguimiento de progreso en tiempo real.



\### Características



\- 🎧 Descarga cualquier vídeo de YouTube como MP3

\- 🔊 Elige la calidad: 128 / 192 / 320 kbps

\- 📊 Barra de progreso en tiempo real

\- 📁 Biblioteca integrada — consulta y vuelve a bajar archivos anteriores

\- 🌑 Interfaz oscura en morado — estética cuidada, todo local

\- ⚡ Sin frameworks, sin npm, sin build



\### Requisitos



\- \*\*Python 3.10+\*\* → \[python.org](https://www.python.org/downloads/)

\- \*\*ffmpeg\*\* instalado y en el PATH



Instala ffmpeg:



| Sistema | Comando |

|---|---|

| Windows | `winget install ffmpeg` |

| macOS | `brew install ffmpeg` |

| Linux | `sudo apt install ffmpeg` |



Comprueba que funciona: `ffmpeg -version`



\### Instalación



```bash

\# 1. Clona el repo

git clone https://github.com/TU\_USUARIO/yt-mp3.git

cd yt-mp3



\# 2. (Opcional pero recomendado) crea un entorno virtual

python -m venv venv

\# Windows

venv\\Scripts\\activate

\# macOS / Linux

source venv/bin/activate



\# 3. Instala las dependencias

pip install -r requirements.txt



\# 4. Arranca

python app.py

```



Luego abre \*\*http://localhost:8000\*\* en el navegador. Listo.



\### Uso



1\. Pega una URL de YouTube en el campo de texto

2\. Selecciona la calidad de audio (192 kbps recomendado para uso general)

3\. Pulsa \*\*Descargar audio\*\*

4\. Mira la barra de progreso — te indica si está descargando o convirtiendo

5\. Cuando termine, pulsa el botón verde para guardar el MP3

6\. Todas tus descargas anteriores aparecen en la sección \*\*Biblioteca\*\*



Los archivos MP3 se guardan en la carpeta `downloads/` dentro del proyecto.



\### Estructura del proyecto



```

yt-mp3/

├─ app.py              # Servidor Flask — gestiona los trabajos y sirve archivos

├─ requirements.txt    # Dependencias Python

├─ downloads/          # Donde se guardan los MP3 (se crea automáticamente)

└─ static/

&#x20;  └─ index.html       # Frontend completo — un solo archivo, sin build

```



\### ⚠️ Importante



Esta app está diseñada \*\*solo para uso local\*\*. No tiene autenticación, ni rate limiting, ni medidas de seguridad. No la expongas en un servidor público.



Descarga únicamente contenido que tengas derecho a descargar.



\---



<div align="center">

Made with 🟣 in Spain

</div>

