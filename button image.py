import tkinter as tk
import customtkinter
import webbrowser


def google_link_opener():
    webbrowser.open("https://google.com/")

root = tk.Tk()

# Load the image
image_path = "files/google.png"  # Replace with the actual path to your image file
image = tk.PhotoImage(file=image_path)

# Create a button with the image
image_button = tk.Button(root, image=image, command=on_button_click)
image_button.pack()

root.mainloop()
