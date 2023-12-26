from tkinter import *
from PIL import ImageTk
import customtkinter
import webbrowser

# Defining the app window 
app = customtkinter.CTk()
app.title("Book Recommendation System For Gutenberg Library")   # This goes to the title bar
customtkinter.set_appearance_mode("dark")                       # 'light', 'dark', 'system'
customtkinter.set_default_color_theme("blue")                   # Themes: "blue", "green", "dark-blue"
# Other themes do work but the dark theme and blue appearance looks better in my opinion.

# This function is checking which main segmented_button is selected in the mainloop and
# it is forgetting all the other except the selected frame and packing that frame in the center of the screen.
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

# This stringVariable takes input from the segmented button and this returns value without needing to use a lambda function
segemented_button_var = customtkinter.StringVar(value=None)
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Search", "List", "Recommend"],
                                                    width=1000, height=35,
                                                    command=segmented_button_callback,
                                                    dynamic_resizing=False,
                                                    corner_radius=10,
                                                    variable=segemented_button_var
                                                    )
# Packing the button in the screen
segemented_button.pack(pady=10) # Padding a little in the top to not touching the title bar

# Setting up the three frames for search list and recommend respectively
frame_search    = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_list      = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_recommend = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)

# Testing to see if the code works or not.
lab2 = customtkinter.CTkLabel(frame_list, text="List")
lab3 = customtkinter.CTkLabel(frame_recommend, text="Recommend")
lab4 = customtkinter.CTkLabel(frame_recommend, text="not Recommend")
lab4.grid(row=2, column=2)
lab2.grid(row=1, column=1)
lab3.grid(row=1, column=1)

# Functions for search frame 
def searchfunction(choice):
    print(choice)

# Search frame 
sbar = customtkinter.CTkEntry(frame_search, placeholder_text="Enter text", width=800)
sbar.grid(row=1, column=1)
s_option = customtkinter.CTkOptionMenu(frame_search, values=['Book Search', 'Author Search'], width=200, command=searchfunction)
s_option.grid(row=1, column=2)

#This frame should contain all the book data after it is printed on the screen
search_scrollable_frame = customtkinter.CTkFrame(frame_search, width = 1000)
search_scrollable_frame.grid(row=2, column=1, columnspan=2, pady=5)












































app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop()