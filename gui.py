

from tkinter import filedialog
from typing_extensions import IntVar
import ytdownloader as yt
import tkinter as tk
from tkinter import BooleanVar, Button, Checkbutton, Label, ttk



window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("600x300")
window.resizable(False, False)
window.grid(widthInc=10, heightInc=10)

dir = filedialog.askdirectory()

label_label = Label(window, text="YouTube Downloader", fg="blue", font="Ubuntu 24")
entry_link = tk.Entry(window, justify='center', name="hhhh", width=40)
combobox_resolutions = ttk.Combobox(window, values=yt.resoloutions, width=9)
button_download = Button(window, text="Download")

# entry_dir = tk.Entry(window, justify='center', name="hhhh", width=30)
button_dir = Button(window, text="Directory")


label_label.place(x=300, y=40, anchor="center")

entry_link.place(x=420, y=140, anchor="se")
combobox_resolutions.place(x=420, y=140, anchor="sw")

button_download.place(x=400, y=200, anchor="center")
button_dir.place(x=200, y=200, anchor="center")

# entry_dir.place(x=420, y=200, anchor="se")

# label_label.pack()
# entry_link.pack()
# combobox_resolutions.pack()

def chose_dir():
  down_dir = filedialog.askdirectory()
   

button_dir.configure(command=chose_dir)


def func():
   link = entry_link.get()
   res = combobox_resolutions.get()
   aud = False
   if res == yt.resoloutions[0]:
      aud = True
   
   print("link : ", link)
   print("res  : ", res)
   print("aud  : ", aud)
   print("dir  : ", dir)

   if yt.download(link=link, res=res, aud=aud, dir=dir) == True:
      print("Successfuly donwloaded")
   else:
      print("Failed")

button_download.configure(command=func)

#--------------------------------------------------------------------------------------------
window.mainloop()