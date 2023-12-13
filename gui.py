from tkinter import *
from PIL import ImageTk
import customtkinter
import webbrowser

# Defining the app window 
app = customtkinter.CTk()
app.title("Book Recommendation System For Gutenberg Library")
# I could not get icon to work for some reason
# icon = ImageTk.PhotoImage(file="files\icon.png")
# app.iconphoto(False, icon)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# The working functions 
def web_open(book):
    url = main.link_return(book)
    webbrowser.open(url, new=2)

def segmented_button_callback(value):
    if value == "Search":
        frame_search.pack()
        frame_list.pack_forget()
        frame_recommend.pack_forget()
    if value == "List":
        frame_search.pack_forget()
        frame_list.pack()
        frame_recommend.pack_forget()
    if value == "Recommend":
        frame_search.pack_forget()
        frame_list.pack_forget()
        frame_recommend.pack()
        

segemented_button_var = customtkinter.StringVar(value=None)
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Search", "List", "Recommend"], width=1000, height=35,
                                                    command=segmented_button_callback, dynamic_resizing=False,
                                                    corner_radius=10,
                                                    variable=segemented_button_var
                                                    )
segemented_button.pack(padx=10,pady=10)

frame_search = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_list = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_recommend = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)

lab2 = customtkinter.CTkLabel(frame_list, text="List")
lab3 = customtkinter.CTkLabel(frame_recommend, text="Recommend")
lab4 = customtkinter.CTkLabel(frame_recommend, text="not Recommend")
lab4.grid(row=2, column=2)
lab2.grid(row=1, column=1)
lab3.grid(row=1, column=1)


# Search frame 
sbar = customtkinter.CTkEntry(frame_search, placeholder_text="Enter text", width=800)
sbar.grid(row=1, column=1)
s_button = customtkinter.CTkButton(frame_search, text="Search", width=200)
s_button.grid(row=1, column=2)



















































app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop()