from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for i in question_data:
    new_q = Question(i["question"], i["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

quiz.end_game()
