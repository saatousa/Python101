from tkinter import *
import pandas
import random

# CONSTANCE
BACKGROUND_COLOR = "#B1DDC6"
COLOR_WHITE = "white"
COLOR_BLACK = "black"
FONT_ITALIC = ("Ariel", 40, "italic")
FONT_BOLD = ("Ariel", 60, "bold")

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# FUNCTIONS:
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_french_card = current_card["French"]
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill=COLOR_BLACK)
    canvas.itemconfig(card_word, text=current_french_card, fill=COLOR_BLACK)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill=COLOR_WHITE)
    canvas.itemconfig(card_word, text=current_card["English"], fill=COLOR_WHITE)


def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)

    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    next_card()



# WINDOW:
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# CANVAS:
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="Title", font=FONT_ITALIC, fill=COLOR_BLACK)
card_word = canvas.create_text(400, 263, text="Word", font=FONT_BOLD, fill=COLOR_BLACK)

canvas.grid(row=0, column=0, columnspan=2)

# BUTTONS:
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
