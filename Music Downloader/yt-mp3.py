import yt_dlp
from pathlib import Path

URL= "https://youtu.be/wAoq__SQpwk"



ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'keepvideo': False,
    'outtmpl': '%(title)s.%(ext)s', 
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        },
        {
            'key': 'FFmpegMetadata', 
        },
        # --- ADD THIS NEW BLOCK ---
        {
            'key': 'FFmpegThumbnailsConvertor',
            'format': 'jpg',  # Converts the .webp to a standard .jpg
        },
        # --------------------------
        {
            'key': 'EmbedThumbnail', 
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    song = ydl.download(URL)

