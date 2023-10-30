import tkinter
import customtkinter
import main


def button_callback():
    label = customtkinter.CTkLabel(app, corner_radius=20, text="Button Pressed")
    label.grid(row=1, column=2)

def bookDataShow():
    ...

app = customtkinter.CTk()
app.geometry("1920x1080")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=1, column=1)
button2 = tkinter.Button(app, text="Hello")
button2.grid(row=1,column=2)
app.mainloop()