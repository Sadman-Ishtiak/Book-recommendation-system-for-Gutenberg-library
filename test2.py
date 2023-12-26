import tkinter as tk

def forget_frame(frame):
    frame.pack_forget()

def create_frames(number_of_frames):
    frames = []
    for i in range(number_of_frames):
        frame = tk.Frame(root, width=300, height=300, bg="lightblue")
        frame.pack(padx=5, pady=5)
        frames.append(frame)
        
        # Create a button to forget the frame
        forget_button = tk.Button(frame, text=f"Forget Frame {i+1}", command=lambda f=frame: forget_frame(f))
        forget_button.pack(pady=5)

    return frames

root = tk.Tk()
root.title("Multiple CTkFrame Objects Example")

# Create 3 frames using the function
created_frames = create_frames(3)

root.mainloop()
