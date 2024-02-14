from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

def play_quiz():
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        question_options = question["incorrect_answers"]
        random_index = random.randint(0, len(question_options))
        question_options.insert(random_index, question_answer)
        options_index = ["A", "B", "C", "D"]
        question_options = zip(options_index, question_options)
        new_question_options = dict(question_options)
        new_question = Question(question_text, question_answer, new_question_options)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    print("Welcome to the Quiz Wonderland! Let's see if you've got the brains to match your enthusiasm!\n")

    if input("Do you want to play? ").lower() != "yes":
        quit()

    print("\nOkay! Let's play.\n")

    while quiz.still_has_question():
        quiz.next_question()

    print("You've completed the quiz!")
    print(f"The Final Score is {quiz.score}/{len(question_bank)}")

    if input("Do you want to play again? ").lower() == "yes":
        play_quiz()

play_quiz()
