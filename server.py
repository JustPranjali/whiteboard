import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter import filedialog
import os

root = Tk()
root.title("WHITE Board")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = "black"
eraser_mode = False  # Track whether eraser mode is active
eraser_image = None  # Image for the eraser

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addline(work):
    global current_x, current_y, color, eraser_mode, eraser_image

    if eraser_mode:
        # Use white color or eraser image for erasing
        if eraser_image:
            canvas.create_image(work.x, work.y, image=eraser_image)
        else:
            canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=root.cget('bg'),
                               capstyle=ROUND, smooth=True)
    else:
        canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color,
                           capstyle=ROUND, smooth=True)

    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color, eraser_mode
    color = new_color
    eraser_mode = False

def activate_eraser():
    global eraser_mode
    eraser_mode = True

def new_canvas():
    canvas.delete("all")
    display_palette()

def insert_image():
    global eraser_image
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetype=(("PNG file", ".png"), ("All files", ".*")))
    if filename:
        eraser_image = PhotoImage(file=filename)

# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# side_bar
color_box = PhotoImage(file="color section.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

eraser = PhotoImage(file="eraser.png")
Button(root, image=eraser, bg="white", command=activate_eraser).place(x=30, y=400)

import_image = PhotoImage(file="addimage.png")
Button(root, image=import_image, bg="white", command=insert_image).place(x=30, y=440)  # Change y-position

colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    id = colors.create_rectangle((10, 10, 30, 30), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("black"))

    id = colors.create_rectangle((10, 40, 30, 60), fill="white")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("white"))

    id = colors.create_rectangle((10, 70, 30, 90), fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("yellow"))

    id = colors.create_rectangle((10, 100, 30, 120), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("red"))

    id = colors.create_rectangle((10, 130, 30, 150), fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("green"))

    id = colors.create_rectangle((10, 160, 30, 180), fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("blue"))

    id = colors.create_rectangle((10, 190, 30, 210), fill="pink")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("pink"))

    id = colors.create_rectangle((10, 220, 30, 240), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("orange"))

    id = colors.create_rectangle((10, 250, 30, 270), fill="gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("gray"))

display_palette()

# main screen
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addline)

# slider
current_value = tk.IntVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()
