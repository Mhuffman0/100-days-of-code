import requests
from html import unescape
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

quiz_params = {"amount": 10, "type": "boolean"}
received = requests.get(url="https://opentdb.com/api.php", params=quiz_params)
received.raise_for_status()
question_data = received.json()["results"]


quiz = QuizBrain(
    [
        Question(unescape(question["question"]), question["correct_answer"])
        for question in question_data
    ]
)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
