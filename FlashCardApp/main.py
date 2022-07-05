import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

# Window
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text((400, 140), text="Language", font=("Ariel", 40, "italic"))
word = canvas.create_text((400, 290), text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

# Wrong Button
wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=2)

# Right Button
right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, borderwidth=0)
right_button.grid(column=1, row=2)

window.mainloop()
