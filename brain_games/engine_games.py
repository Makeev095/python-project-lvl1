import prompt
from brain_games.scripts.brain_calc import calc


def run(game):
    game = calc
    right_answers = 0
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    for right_answers in range(3):
        res, result = game.discription()
        print(game.game_question())
        print(result)
        answer = prompt.string("Your answer: ")
        if int(answer) == res:
            print("Correct!")
            right_answers += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
