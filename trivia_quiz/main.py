from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data[0]["results"]:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

random.shuffle(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
