

from pytube import YouTube
import traceback as tb
from sys import stderr
from os import path
from os import mkdir

link = 'https://www.youtube.com/watch?v=Wjrrgrvq1ew'
dir = "./downloads"
resoloutions = ['Audio (mp4)','240p','360p','480p','720p','1080p','1440p','2160p']


def download(link=link, res='720p', aud=False, dir=dir):
   """
      Downloads a YouTube video as a vides with given resolution
      or as audio format.
      If an error occured or exception raised, False is returned,
      alse it return True (video has been downloaded)

      PARAMETERS
         link  : link of the video\n
         res   : wanted resolution for donwnload (default: '720p')\n
         aud   : boolean for audio converting (True : download only mp4 audio)\n
         dir   : directoy for downloaded files\n
   
   """
   if not path.exists(dir):
      mkdir(dir)

   try:
      yt = YouTube(link)
      ys = yt.streams
      print(dir)
      if aud == True:
         ysf = ys.get_audio_only()
      elif aud == False:
         ysf = ys.get_by_resolution(resolution=res)
      ysf.download()
      print("Downloaded successfully")
      return True
   except AttributeError as e:
      # print(e)
      print(f"The resolution [{res}] is not available for this video", file=stderr)
      
      return False
   except Exception as e:
      print("Not working !!", file=stderr)
      # print(e)
      # tb.print_exception(tb.format_exc(), file=stderr)
      return False


link = 'https://www.youtube.com/watch?v=Wjrrgrvq1ew'

# # download(aud=True)
# download(res='240p', dir='./')
# download()