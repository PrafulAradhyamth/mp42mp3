import tkinter as tk
from tkinter import filedialog
import os
import re
from moviepy.editor import *
from tkinter import messagebox

def testi():
    try:
        mp4_file = filedialog.askopenfilenames(parent=root,initialdir='/',initialfile='what paa no mannersaa',filetypes=[("MP4", "*.mp4"),("All files", "*")])
        mp4_file=mp4_file[0]
        mp3_file=re.sub('mp4','mp3',mp4_file)
        videoclip=VideoFileClip(mp4_file)
        audioclip=videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
    except:
            messagebox.showerror('la faute','You didnt select any file')
    return

root =tk.Tk()
root.title('musique')
root.iconbitmap('icon.ico')
background_image=tk.PhotoImage(file='background.png')
background_label=tk.Label(root,image=background_image)
background_label.pack()
button=tk.Button(root,text='Select the Mp4 file to be converted',command=testi)
button.place(relx=0.4,rely=0.85,relwidth=0.5,relheight=0.1)
root.mainloop()