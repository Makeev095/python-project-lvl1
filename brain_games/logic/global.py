from brain_games.games.calc import calc_description
from brain_games.games.cli import welcome_user
import prompt


def run(game):
    answer, result, task = calc_description()
    welcome_user()
    name = prompt.string('May I have your name? ')
    print(task)
    right_answers = 0
    for right_answers in range(3):
        answer = prompt.string("Your answer: ")
        if int(answer) == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
        print(f"Congratulations, {name}!")
