

from tkinter import filedialog
import ytdownloader as yt
import tkinter as tk
from tkinter import  Button, Label, ttk
import pyperclip as ppc


class Gui(tk.Frame):

   dir = None
   label_label = None
   label_auth = None
   label_msg = None
   entry_link = None
   combobox_resolutions = None
   button_download = None
   entry_dir = None
   button_dir = None
   button_paste = None
   resoloutions = ['Audio (mp4)','240p','360p','480p','720p','1080p','1440p','2160p']

   def __init__(self, window) -> None:
      window.title("YouTube Downloader")
      window.geometry("600x300")
      window.resizable(False, False)
      window.grid(widthInc=10, heightInc=10)
      tk.Frame.__init__(self, window)
      self.window = window

   def show(self):
      self.label_label = Label(self.window, text="YouTube Downloader", bg="#c7000a", fg ="#ffffff", width=600, font="Ubuntu 24", height=2)
      auth = "By: Abdelhaq El Amraoui  Ⓒ2021  |   For error reports please visit :   www.elam-2020.blogspot.com"
      self.label_auth = Label(self.window, text=auth, font="Ubuntu-Mono 8", bg="#c3c4c4", width=600)
      self.label_msg = Label(self.window, font="Calibri 9", fg='green')
      self.entry_link = tk.Entry(self.window, justify='left', width=42)
      self.combobox_resolutions = ttk.Combobox(self.window, values=self.resoloutions, state='readonly', width=10, background='red')
      self.combobox_resolutions.current(4) #setting '720p' as default value
      self.button_download = Button(self.window, text="Download", command=self.func, bg='#114F74', fg='#ffffff')
      msg = 'Please select a directory'
      self.label_dir = Label(self.window, justify='left', width=100, font='Ubuntu 10' ,text=msg)
      self.button_dir = Button(self.window, text="Directory", command=self.chose_dir, bg='#114F74', fg='#ffffff')
      self.button_paste = Button(self.window, text="Paste link", command=self.paste_link, bg='#114F74', fg='#ffffff')
    
      self.label_label.place(x=300, y=0, anchor="n")
      self.label_auth.place(x=300, y=300, anchor="s")
      self.label_msg.place(x=300, y=98, anchor="center")

      self.entry_link.place(x=420, y=140, anchor="se")
      self.combobox_resolutions.place(x=420, y=140, anchor="sw")
      self.label_dir.place(x=300, y=170, anchor="center")
      self.button_dir.place(x=170, y=220, anchor="center")
      self.button_paste.place(x=290, y=220, anchor="center")
      self.button_download.place(x=410, y=220, anchor="center")

   def chose_dir(self):
      self.dir = filedialog.askdirectory()
      self.label_dir.configure(text=self.dir)
      self.label_msg.configure(text=' ')

   def paste_link(self):
      self.entry_link.delete(0, 'end')
      self.entry_link.insert(0, ppc.paste())
      self.label_msg.configure(text=' ')
   
      

   def func(self):
         link = self.entry_link.get()
         res = self.combobox_resolutions.get()
         aud = False
         if res == self.resoloutions[0]:
            aud = True
         dir = self.dir

         if link == None or dir == None:
            return

         d = yt.Download(link=link, res=res, aud=aud, dir=dir)
         
         self.label_msg.configure(text="Downloading...", fg='green')

         try:
            d.start()
         except Exception as e:
            self.label_msg.configure(text=str(e), fg='red')
         else:
            self.label_msg.configure(text="Completed successfully", fg='green')

#*******************************************************************************
window = tk.Tk()

g = Gui(window)
g.show()

window.mainloop()