import tkinter as tk
import random

root = tk.Tk()
root.title("Downloading . . .")
root.geometry("450x300")

label = tk.Label(root, text="Slide to download more RAM", font=("Helvetica", 30))
label.pack(pady=20) #.pack() makes sure the element show

slider_value = tk.IntVar()

message_label = tk.Label(root, text="", font=("Helvetica", 12))
message_label.pack(pady=20)

def check_slider(value):
    if int(value) == 99:
        message_label.config(text="Your free trial has expired. Cancel your subscription by clicking below")
        slider.config(state="disabled")  # disable the slider once hits 100
        button = tk.Button(root, text="Cancel purchase", font=("Helvetica", 16))
        button.place(x=175, y=220)
        def move_button(event):
            new_x = random.randint(0, 300)
            new_y = random.randint(0, 220)
            button.place(x=new_x, y=new_y)

# bind hover/enter event 
        button.bind("<Enter>", move_button)
        

slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300,
                  variable=slider_value, showvalue=True, command=check_slider)
slider.pack()


root.mainloop()