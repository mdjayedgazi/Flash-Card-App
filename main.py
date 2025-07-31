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
card_img  = PhotoImage(file="images/card_front.png")

# Card Canvas 
canvas = Canvas(width=800,height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400,263,image = card_img)
canvas.grid(row=0,column=0,columnspan=2)
canvas.create_text(400,148,text="Title",font=("Ariel",40,"italic"))
canvas.create_text(400,290,text="Word",font=("Ariel",60,"bold"))
# Button 
wrong_button = Button(image=Wrong_img,highlightthickness=0,bd=0)
wrong_button.grid(row=1,column=0,pady=10)

right_button = Button(image=Right_img,highlightthickness=0,bd=0)
right_button.grid(row=1,column=1,pady=10)

root.mainloop()