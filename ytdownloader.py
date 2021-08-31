

from pytube import YouTube

def download(link):
  
   try:
      yt = YouTube(link)
      ys = yt.streams
      first_video = ys.first()
      first_video.download()
   except Exception:
      print("Not working !!")
   else:
      print(f"{yt.title} has been downloaded !")

link = 'https://www.youtube.com/watch?v=Wjrrgrvq1ew'

download(link)
