from data import question_data as data
from question_model import Question
from quiz_brain import QuizBrain as qb


question_bank = []

for question in data:
    text = question["text"]
    answer = question["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = qb(question_bank)
while quiz.still_has_questions():
    qb.next_question(quiz)

