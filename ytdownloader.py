

from pytube import YouTube
import traceback as tb
from os import path
from os import mkdir



class Download:
   _link = 'https://www.youtube.com/watch?v=Wjrrgrvq1ew'
   _dir = "./downloads"
   message = "fff"

   def __init__(self, link=_link, res='720p', aud=False, dir=dir) -> None:
      self.link = link
      self.res = res
      self.aud = aud
      self.dir = dir

   def start(self):
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
      if not path.exists(self.dir):
         mkdir(self.dir)

      try:
         yt = YouTube(self.link)
         ys = yt.streams
         if self.aud == True:
            ysf = ys.get_audio_only()
         elif self.aud == False:
            ysf = ys.get_by_resolution(resolution=self.res)
         ysf.download(self.dir)
         self.message = "Downloaded successfully"
         return True
      except AttributeError as e:
         self.message = f"Resolution [{self.res}] is not available for this video"
         return False
      except Exception as e:
         self.message = "Not working !!"
         return False

   @property
   def get_message(self):
      return self.message


link = 'https://www.youtube.com/watch?v=Wjrrgrvq1ew'

# # download(aud=True)
# download(res='240p', dir='./')
# download()

# d = Download(aud=True, dir='.')
# print(d.get_message)
# d.start()
# print(d.get_message)