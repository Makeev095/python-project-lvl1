from brain_games.games.calc import calc_description, calc_generate
from brain_games.games.cli import welcome_user
import prompt


def run(task, result):
    welcome_user
    name = prompt.string('May I have your name? ')
    print(task)
    right_answers = 0
    while right_answers != 3:
        print(calc_description)
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
