import tkinter
import customtkinter
import webbrowser
import main

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def web_open(book):
    url = main.link_return(book)
    webbrowser.open(url, new=2)

def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button_var = customtkinter.StringVar(value=None)
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
                                                    command=segmented_button_callback, dynamic_resizing=False,
                                                    width=1920,height=30, variable=segemented_button_var
                                                    )
segemented_button.pack()

app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop()