import tkinter
import time

# ---------------------------- CONSTANTS ------------------------------- #
# colorhunt
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    checkmarks.configure(text="")
    setup_header(work_label)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps < 9:
        reps += 1
    # print(reps)

    if reps % 8 == 0 and reps > 0:
        count_down(LONG_BREAK_MIN * 60)
        work_label.configure(text="Break", fg=PINK)

    elif reps % 2 == 0 and reps < 8:
        count_down(SHORT_BREAK_MIN * 60)
        work_label.configure(text="Break", fg=GREEN)

    elif reps < 8:
        count_down(WORK_MIN * 60)
        work_label.configure(text="Work", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    if seconds >= 0:
        window.after(10, count_down, seconds - 1)
        canvas.itemconfig(timer_text, text=f"{seconds//60}:{seconds%60:02d}")
    else:
        checkmarks.configure(text="✓" * (reps // 2))
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=34, pady=10, bg=YELLOW)

# Header
def setup_header(label):
    label.configure(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))


work_label = tkinter.Label()
setup_header(work_label)

work_label.grid(column=1, row=0)

# Tomato
tomato = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(
    100, 128, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Start Button
start_button = tkinter.Button(
    text="Start", font=(FONT_NAME, 12), bg="white", command=start_timer
)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tkinter.Button(
    text="Reset", font=(FONT_NAME, 12), bg="white", command=reset_timer
)
reset_button.grid(column=2, row=2)

# Checkmark
checkmarks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
checkmarks.grid(column=1, row=3)

window.mainloop()
