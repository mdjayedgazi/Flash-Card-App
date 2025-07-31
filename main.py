from tkinter import*
from tkinter import messagebox
import pandas as pd
import random
import json

BACKGROUND_COLOR = "#B1DDC6"

# # ------------------------ UI SETUP ----------------------- # #
root = Tk()
root.title("Flash Card")
root.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
# Load images(use raw strings or forward slashes)
Right_img = PhotoImage(file="images/right.png")
Wrong_img = PhotoImage(file="images/wrong.png")
card_img = PhotoImage(file="images/card_front.png")

# Card Canvas 
canvas = Canvas(width=800,height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400,263,image = card_img)
canvas.grid(row=0,column=0,columnspan=2)

#Labels (centered on card)
con_label = Label(text="French",font=("Arial",40,"italic"),bg="white")
con_label.place(x=400,y=100,anchor='center')

word_label = Label(text="trouve",font=("Arial",60,"bold"),bg="white")
word_label.place(x=400,y=263,anchor="center")

# Button 
wrong_button = Button(image=Wrong_img,highlightthickness=0,borderwidth=0)
wrong_button.grid(row=1,column=0,pady=10)

right_button = Button(image=Right_img,highlightthickness=0,borderwidth=0)
right_button.grid(row=1,column=1,pady=10)

root.mainloop()