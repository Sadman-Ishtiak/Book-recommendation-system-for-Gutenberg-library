import tkinter as tk
from PIL import Image, ImageTk

def quitGame(event):
    print("YO")

window = tk.Tk()
window.geometry("1000x1000")

canvas = tk.Canvas(window, width = 300, height = 300)
canvas.pack()

#creating background
bgImage = ImageTk.PhotoImage(Image.open("files/yoyo.png")) 
bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

#creating button which supports png transparency
quitImage = ImageTk.PhotoImage(Image.open("files/google.png"))
quitButton = canvas.create_image(500, 500, image=quitImage)
canvas.tag_bind(quitButton, "<Button-1>", quitGame)

window.mainloop()