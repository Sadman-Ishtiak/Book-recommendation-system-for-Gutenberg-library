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
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Search", "List", "Recommend"],
                                                    command=segmented_button_callback, dynamic_resizing=False,
                                                    width=1920,height=30, variable=segemented_button_var
                                                    )
segemented_button.pack()

frame_search = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_list = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_recommend = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)

lab1 = customtkinter.CTkLabel(frame_search, text="SEARCH")
lab2 = customtkinter.CTkLabel(frame_list, text="List")
lab3 = customtkinter.CTkLabel(frame_recommend, text="Recommend")
lab1.pack()
lab2.pack()
lab3.pack()


app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop()