import tkinter
import customtkinter
import webbrowser
import main
# Defining the app window 
app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# The working functions 
def web_open(book):
    url = main.link_return(book)
    webbrowser.open(url, new=2)






# The GUI PART
tabview = customtkinter.CTkTabview(master=app,height=200,width=200)
tabview.pack(padx=20, pady=20)

tab_search = tabview.add("Search")  # add tab at the end
tab_my_books = tabview.add("My Books")  # add tab at the end
tab_recommend = tabview.add("Recommend")
# tabview.set("Search")

button = customtkinter.CTkButton(master=tab_search)
button.pack(padx=20, pady=20)




































































# Final mainloop to put that in GUI
app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop()