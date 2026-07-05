<div align="center">

```
██╗   ██╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗
╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝    ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
  ╚██╔╝     ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
   ██║      ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
   ╚═╝      ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```

**[ MP3 / MP4 EXTRACTION UTILITY — BUILT ON YT-DLP ]**

![Python](https://img.shields.io/badge/python-3.8+-00FF41?style=flat-square\&logo=python\&logoColor=black\&labelColor=0D0D0D)
![yt-dlp](https://img.shields.io/badge/yt--dlp-required-00FF41?style=flat-square\&labelColor=0D0D0D)
![FFmpeg](https://img.shields.io/badge/ffmpeg-required-00FF41?style=flat-square\&labelColor=0D0D0D)
![Deno](https://img.shields.io/badge/deno-required-00FF41?style=flat-square\&labelColor=0D0D0D)
![License](https://img.shields.io/badge/license-MIT-00FF41?style=flat-square&labelColor=0D0D0D)

</div>

---

## > SYSTEM\_OVERVIEW

A Python CLI tool that connects to the YouTube data stream and extracts either the full **MP4** signal (with selectable resolution) or an isolated **MP3** audio channel (with selectable bitrate).

```
[+] Download video as MP4 — choose resolution (1080p / 720p / 480p / ...)
[+] Extract audio as MP3 — choose bitrate (320 / 256 / 192 / 128 kbps)
[+] Interactive prompts — no flags to memorize
[+] Auto-handles YouTube bot-check via browser cookies or cookies.txt
```

---

## > REQUIREMENTS

|Component|Purpose|
|-|-|
|**Python 3.8+**|Runtime environment|
|[**yt-dlp**](https://github.com/yt-dlp/yt-dlp)|Core extraction engine|
|[**FFmpeg**](https://ffmpeg.org/)|Merges video/audio streams, converts to MP3|
|[**Deno**](https://deno.com/)|Solves YouTube's JS "n challenge" — without it, only thumbnails are reachable|

---

## > INSTALLATION

### [1] Install the Python package

```bash
pip install yt-dlp
```

### [2] Install FFmpeg

```bash
# Windows
winget install ffmpeg

# macOS
brew install ffmpeg

# Linux
sudo apt install ffmpeg
```

### [3] Install Deno

```bash
# Windows (PowerShell)
irm https://deno.land/install.ps1 | iex

# macOS
brew install deno

# Linux
curl -fsSL https://deno.land/install.sh | sh
```

> Restart your terminal fully after installing Deno so the system PATH is refreshed.

### [4] Execute

```bash
python YTDownloader.py
```

---

## > USAGE

```
1. Run the script and paste a YouTube URL when prompted
2. Select output format  →  MP4 (video)  or  MP3 (audio)
3. Select quality        →  resolution (MP4)  or  bitrate (MP3)
4. Select destination folder, or press Enter to use the current directory
```

---

## > TROUBLESHOOTING: "Sign in to confirm you're not a bot"

YouTube occasionally flags automated requests and demands login verification. When triggered, the script offers two authentication paths:

```
[1] Browser cookies   — browser must be FULLY closed (check background processes too)
[2] cookies.txt file  — exported manually, more reliable
```

### >> Correctly exporting `cookies.txt`

YouTube rotates account cookies as a security measure -- cookies pulled from an already-open, regular browser tab may be dead on arrival. Follow this sequence exactly:

```
[1] Open a new Browsing window with an unofficial or a second Google account
[2] Open the video you want to download from youtube
[3] Watch the Ads to make a temporary token
[4] Export the youtube.com cookies using an extension
    (e.g. "Get cookies.txt LOCALLY")
[5] Point the script to the exported cookies.txt path
```



## > OR Quick start:

> Don't want to set up Python? Skip the installation steps above and

> [download the prebuilt standalone `LastVersion.exe`] from [here...](https://github.com/CryptoskinR/YTDownloader/releases/download/v1.1.0/YTDownloader-standalone1.1.0.exe)

> Just keep in mind FFmpeg and Deno are still required separately (see step 2 and 3 above).

> Windows only for now.

> **⚠️Windows SmartScreen may flag this file since it's unsigned and newly published⚠️**

> Click "More info" → "Run anyway" to proceed.
> This is expected for new open-source executables and does not indicate malware.



## > DISCLAIMER

This project is provided for **educational and personal-use purposes only**.

* The author does not host, store, or distribute any copyrighted content.
* Users are solely responsible for ensuring they have the legal right to download
any content they access with this tool (e.g. their own uploads, public domain
material, or content explicitly licensed for download such as Creative Commons).
* Downloading copyrighted material without permission from the rights holder may
violate copyright law and/or YouTube's Terms of Service in your jurisdiction.
* This software is provided "as is", without warranty of any kind. The author is
not liable for any misuse of this tool or any consequences resulting from its use.

By using this tool, you agree that you understand and accept full responsibility
for how it is used.

---

> **Note:** Use a secondary/throwaway Google account for this process rather than your main account. Exporting and reusing session cookies carries a small risk of the account being flagged or temporarily restricted by YouTube.

---

<div align="center">

*This tool is intended for content you own or have explicit permission to download. Copyright laws and YouTube's Terms of Service vary by jurisdiction -- **use responsibly**.*

</div>

