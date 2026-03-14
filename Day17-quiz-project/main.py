from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"].lower()))

quiz = QuizBrain(question_bank)
while quiz.has_next_question():
    quiz.next_question()
