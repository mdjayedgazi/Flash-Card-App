from tkinter import*
from tkinter import messagebox
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
# # --------------------------- READ THE DATA FILE ------------- # #
data_file = pd.read_csv("data/french_words.csv")
to_learn = data_file.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text= "French")
    canvas.itemconfig(card_word,text= current_card["French"])
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
card_title = canvas.create_text(400,148,font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,290,font=("Ariel",60,"bold"))
# Button 
wrong_button = Button(image=Wrong_img,highlightthickness=0,bd=0,command=next_card)
wrong_button.grid(row=1,column=0,pady=10)

right_button = Button(image=Right_img,highlightthickness=0,bd=0,command=next_card)
right_button.grid(row=1,column=1,pady=10)
next_card()

root.mainloop()