from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Try to open updated words.
# If file doesn't exist, open original data.
# Either way convert to dictionary.
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --- WORDS TO LEARN --- #
# Remove current word form dictionary if known button is clicked.
# Index set to false to avoid recurring indexing.
def word_known():
    to_learn.remove(current_card)
    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("words_to_learn.csv", index=False)
    next_card()


# --- CHANGE CARDS --- #
def next_card():
    global current_card, timer
    # Reset timer is next card is selected before 3 seconds.
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    # Replace canvas values.
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_image, image=front_img)
    # Turn card after 3 seconds.
    timer = window.after(3000, func=turn_card)


def turn_card():
    # Replace canvas values.
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# --- CREATE UI --- #

# Screen
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Wait for 3 seconds before turning card
timer = window.after(3000, func=turn_card)

# Card Images
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Spanish Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=word_known)
right_btn.grid(column=1, row=1)

# Call next card in order to load random when program is run.
next_card()

window.mainloop()