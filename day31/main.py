from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
data = pandas.read_csv("./data/words_to_learn.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
#----------------------------FLASH CARDS---------------------------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(flash_card, image=card_front_img)
    screen.after(3000, func=flip_card)

#----------------------------FLIP CARDS---------------------------------------
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(flash_card, image=card_back_img)

#----------------------------SAVE PROGRESS---------------------------------------

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()




#----------------------------CREATE UI---------------------------------------
screen = Tk()
screen.title("Learning French Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
flash_card = canvas.create_image(400, 260, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=is_known)
right_button.grid(row=1, column=1)

next_card()
is_known()







screen.mainloop()