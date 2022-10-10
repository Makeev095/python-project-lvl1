import prompt
from brain_games.games import prime
from brain_games.games import calc
from brain_games.games import even
from brain_games.games import progression
from brain_games.games import gcd


def run(game):
    game = prime
    right_answers = 0
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    question = game.game_question()
    print(question)
    for right_answers in range(3):
        res, result = game.discription()
        print(result)
        answer = game.getting_answer()
        if answer == res:
            print("Correct!")
            right_answers += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
