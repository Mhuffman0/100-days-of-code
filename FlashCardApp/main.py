import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
to_learn = df.to_dict(orient="records")

current_word = None


def flip_card(language, text_color, card_image):
    canvas.itemconfig(language_text, text=language, fill=text_color)
    canvas.itemconfig(card, image=card_image)
    canvas.itemconfig(word_text, text=current_word[language], fill=text_color)


def flip_card_back():
    flip_card(language="English", text_color="white", card_image=card_back)


def flip_card_front():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    flip_card(language="French", text_color="black", card_image=card_front)
    flip_timer = window.after(3000, flip_card_back)


def is_known():
    to_learn.remove(current_word)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    flip_card_front()


# Window
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card_back)

# Canvas
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263)
language_text = canvas.create_text(
    (400, 140), text="French", font=("Ariel", 40, "italic")
)
word_text = canvas.create_text((400, 290), text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)
flip_card_front()


# Wrong Button
wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(
    image=wrong_image, highlightthickness=0, borderwidth=0, command=flip_card_front
)
wrong_button.grid(column=0, row=2)

# Right Button
right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(
    image=right_image, highlightthickness=0, borderwidth=0, command=is_known
)
right_button.grid(column=1, row=2)


window.mainloop()
