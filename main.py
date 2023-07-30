from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# the text returned from an API contains HTML entities so we can use -> https://www.freeformatter.com/html-escape.html to unescape the html response
quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)

