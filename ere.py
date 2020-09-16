import tkinter as tk
import os
from tkinter import filedialog
from moviepy.editor import *
import re
from tkinter import messagebox



Height=300
Width=500

def testi():
    try:
        mp4_file = filedialog.askopenfilenames(parent=root,initialdir='/',initialfile='tmp',filetypes=[("MP4", "*.mp4"),("All files", "*")])
        mp4_file=mp4_file[0]
        mp3_file = re.sub('mp4', 'mp3', mp4_file)
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
    except:
        messagebox.showinfo("la faute", "You didn't select any file")
            
    return
    
    
root=tk.Tk()


root.title("Converter")
root.iconbitmap('icon.ico')

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.pack()


button = tk.Button(root,text="Select MP4 to Convert",command=testi)
button.place(relx=0.38, rely=0.8, relwidth=0.3, relheight=0.1)

root.mainloop()