import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Setup Canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            (150, 125),
            text="",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Setup true button
        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(
            image=true_image,
            highlightthickness=0,
            borderwidth=1,
            command=self.true_button_click,
        )
        self.true_button.grid(row=2, column=0)

        # Setup false button
        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(
            image=false_image,
            highlightthickness=0,
            borderwidth=1,
            command=self.false_button_click,
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
            return None
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.canvas.itemconfig(self.question_text, text=f"Final Score: {self.quiz.score}/10")

    def button_click(self, answer):
        is_right = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

    def true_button_click(self):
        self.button_click("True")

    def false_button_click(self):
        self.button_click("False")
