import yt_dlp as youtube_dl
from yt_dlp import YoutubeDL
# def descargar_videos(url):
#     ydl_opt = {

#         'format': 'best',
#         'outtmpl': '%(title)s.%(ext)s',

#     }
#     with youtube_dl.YoutubeDL(ydl_opt) as ydl:
#         ydl.download([url])

# url = "https://youtu.be/11DCciucXFs"
# descargar_videos(url)
YoutubeDL().download("https://youtu.be/11DCciucXFs")