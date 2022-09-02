from brain_games.games.calc import *
from brain_games.games.cli import welcome_user
import prompt


def run(task_1, result, name, answer, question_calc):
    welcome_user()
    name = prompt.string('May I have your name? ')
    print(task_1)
    right_answers = 0
    while right_answers != 3:
        calc_description()
        print(question_calc)
        answer = prompt.string("Your answer: ")
        calc_generate()
    if int(answer) == result:
        right_answers += 1
        print("Correct!")
    else:
        print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
        right_answers = 0
        return 0
    print(f"Congratulations, {name}!")
