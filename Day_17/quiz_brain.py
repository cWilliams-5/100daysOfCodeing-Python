class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.correct = 0

    def still_has_questions(self):
        count = 0
        for i in self.questions_list:
            count += 1
        if self.question_number < count:
            print(f"Your current score is: {self.correct}/{self.question_number}")
            return True
        else:
            print(f"Quiz Complete. Final Score = {self.correct}/{self.question_number} ")
            return False
    def next_question(self):
        q = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {q.text} (True/False)")
        if answer == q.answer:
            self.correct += 1
            print(f"Correct!\nThe correct answer was: {q.answer}")
        else:
            print(
                f"Inorrect.\nThe correct answer was: {q.answer}")







