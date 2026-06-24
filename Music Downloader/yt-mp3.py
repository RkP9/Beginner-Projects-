import yt_dlp
import os 

URL= "Youtube Link"

save_file = "your/file/path"

os.makedirs(save_file, exist_ok = True)

ydl_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'keepvideo': False,
    'outtmpl': os.path.join(save_file, '%(title)s.%(ext)s'), 
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        },
        {
            'key': 'FFmpegMetadata', 
        },
        {
            'key': 'FFmpegThumbnailsConvertor',
            'format': 'jpg', 
        },
        {
            'key': 'EmbedThumbnail', 
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    song = ydl.download([URL])