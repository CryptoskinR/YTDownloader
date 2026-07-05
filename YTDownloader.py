#!/usr/bin/env python3
"""
YTDownloader with MP3 / MP4 format and quality selection
Requires: yt-dlp and ffmpeg
"""

import os
import sys

try:
    import yt_dlp
except ImportError:
    print("The yt-dlp library is not installed. Run this command first:")
    print("    pip install yt-dlp")
    sys.exit(1)


def get_base_opts(cookies_browser=None, cookies_file=None):
    """Shared base options for info-fetching and downloading"""
    opts = {
        "quiet": True,
        # Allow yt-dlp to download the EJS challenge-solver script from GitHub.
        # Required for YouTube's JS "n challenge" (needed to get real video/audio
        # formats instead of just thumbnail images). See: yt-dlp/yt-dlp wiki/EJS
        "remote_components": {"ejs:github"},
    }
    if cookies_file:
        opts["cookiefile"] = cookies_file
    elif cookies_browser:
        opts["cookiesfrombrowser"] = (cookies_browser,)
    return opts


def get_video_info(url, cookies_browser=None, cookies_file=None):
    """Fetch video info and available formats"""
    with yt_dlp.YoutubeDL(get_base_opts(cookies_browser, cookies_file)) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def choose_cookies_method():
    print("\nYouTube sometimes requires login verification to block automated downloads.")
    print("If you're hitting 'Sign in to confirm you're not a bot', you have two options:\n")
    print("  1) Use cookies directly from a browser (the browser must be FULLY closed, check Task Manager too)")
    print("  2) Provide the path to a cookies.txt file you exported yourself (more reliable)")
    print("  3) Skip this step\n")
    method = input("Choice (1/2/3): ").strip()

    if method == "1":
        browsers = ["chrome", "firefox", "edge", "brave", "opera", "vivaldi", "safari"]
        for i, b in enumerate(browsers, 1):
            print(f"  {i}) {b}")
        choice = input("Browser number: ").strip()
        try:
            return browsers[int(choice) - 1], None
        except (ValueError, IndexError):
            print("Invalid choice.")
            return None, None

    elif method == "2":
        path = input("Enter the full path to your cookies.txt file: ").strip()
        if path and os.path.isfile(path):
            return None, path
        print("File not found.")
        return None, None

    return None, None


def list_video_qualities(info):
    """Extract available video qualities (formats that include video)"""
    heights = set()
    for f in info.get("formats", []):
        if f.get("vcodec") != "none" and f.get("height"):
            heights.add(f["height"])
    return sorted(heights, reverse=True)


def choose_output_folder():
    folder = input("Destination folder to save the file (press Enter for current folder): ").strip()
    if not folder:
        folder = os.getcwd()
    os.makedirs(folder, exist_ok=True)
    return folder


def download_mp4(url, height, out_folder, cookies_browser=None, cookies_file=None):
    ydl_opts = get_base_opts(cookies_browser, cookies_file)
    ydl_opts.update({
        "format": f"bestvideo[height<={height}]+bestaudio/best[height<={height}]",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(out_folder, "%(title)s.%(ext)s"),
        "progress_hooks": [progress_hook],
    })
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_mp3(url, bitrate, out_folder, cookies_browser=None, cookies_file=None):
    ydl_opts = get_base_opts(cookies_browser, cookies_file)
    ydl_opts.update({
        "format": "bestaudio/best",
        "outtmpl": os.path.join(out_folder, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": str(bitrate),
            }
        ],
        "progress_hooks": [progress_hook],
    })
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "").strip()
        print(f"\rDownloading... {percent}  speed: {speed}", end="")
    elif d["status"] == "finished":
        print("\nDownload finished, post-processing...")


def main():
    print("=== YTDownloader ===\n")
    url = input("Enter the YouTube video URL: ").strip()
    if not url:
        print("No URL entered. Exiting.")
        return

    cookies_browser = None
    cookies_file = None
    print("\nFetching video info...")
    try:
        info = get_video_info(url)
    except Exception as e:
        err_text = str(e)
        if "Sign in to confirm" in err_text or "bot" in err_text.lower():
            print("YouTube is requesting login verification.")
            cookies_browser, cookies_file = choose_cookies_method()
            if cookies_browser or cookies_file:
                try:
                    info = get_video_info(url, cookies_browser, cookies_file)
                except Exception as e2:
                    print(f"Error fetching video info (with cookies): {e2}")
                    print("\nIf using Chrome cookies, make sure Chrome is FULLY closed")
                    print("(check Task Manager for any leftover chrome.exe process)")
                    print("or use the cookies.txt export method instead.")
                    print("\nIf using cookies.txt, make sure you exported it WHILE on")
                    print("youtube.com and logged in (not from another tab/site).")
                    return
            else:
                print("Cannot continue without cookies. Exiting.")
                return
        else:
            print(f"Error fetching video info: {e}")
            return

    title = info.get("title", "Unknown")
    print(f"Video title: {title}\n")

    print("Choose the output format:")
    print("  1) MP4 (video)")
    print("  2) MP3 (audio only)")
    choice = input("Choice (1 or 2): ").strip()

    out_folder = choose_output_folder()

    if choice == "1":
        qualities = list_video_qualities(info)
        if not qualities:
            print("No quality options found for this video.")
            return
        print("\nAvailable qualities:")
        for i, q in enumerate(qualities, 1):
            print(f"  {i}) {q}p")
        idx = input("Enter the number of the quality you want: ").strip()
        try:
            height = qualities[int(idx) - 1]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return
        print(f"\nDownloading at {height}p...")
        download_mp4(url, height, out_folder, cookies_browser, cookies_file)

    elif choice == "2":
        print("\nChoose the audio quality (bitrate):")
        bitrates = ["320", "256", "192", "128"]
        for i, b in enumerate(bitrates, 1):
            print(f"  {i}) {b} kbps")
        idx = input("Enter the number of the quality you want: ").strip()
        try:
            bitrate = bitrates[int(idx) - 1]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return
        print(f"\nDownloading audio at {bitrate} kbps...")
        download_mp3(url, bitrate, out_folder, cookies_browser, cookies_file)

    else:
        print("Invalid choice.")
        return

    print(f"\n✅ File saved successfully to:\n{out_folder}")


if __name__ == "__main__":
    while True:
        main()
        print("\nDo you want to download another link?")
        print("  1) Yes")
        print("  2) No")
        again_choice = input("Choice (1 or 2): ").strip()
        if again_choice == "1":
            print("\n" + "-" * 50 + "\n")
            continue
        else:
            print("\nThank you for using YTDownloader!")
            print("Press any key to exit...")
            try:
                import msvcrt
                msvcrt.getch()
            except ImportError:
                input()
            break
