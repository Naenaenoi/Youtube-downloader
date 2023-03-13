import tkinter
import customtkinter as ctk
from pytube import YouTube

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x300")
app.title("YTD")

options_var = ctk.StringVar(value = "MP4")

def options_callback(choice):
    if choice == 'MP4':
        Video_download()
    elif choice == 'MP3':
        Audio_download()

options = ctk.CTkOptionMenu(app, values = ["MP4", "MP3"], command = options_callback, variable = options_var)
options.pack(padx = 20, pady = 10)


def Video_download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        video.download(output_path="Videos")
        finishLabel.configure(text="Download Complete")
    except:
        finishLabel.configure(text="INVALID LINK YOU FUCK!!!!!")

def Audio_download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title)
        audio.download(output_path="Audio")
        finishLabel.configure(text="Download Complete")
    except:
        finishLabel.configure(text="INVALID LINK YOU FUCK!!!!!")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)


title = ctk.CTkLabel(app, text = "Input link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable = url_var)
link.pack()

finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack()

pPercentage = ctk.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = ctk.CTkButton(app, text="Download", command= Video_download)
download.pack(padx=10, pady=10)




app.mainloop()