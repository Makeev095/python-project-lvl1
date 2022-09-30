import prompt
from brain_games.games import calc
from brain_games.games import gcd
from brain_games.games import prime
from brain_games.games import even
from brain_games.games import progression



def run(game):
    name = prompt.string('May I have your name? ')
    right_answers = 0
    for right_answers in range(3):
        question = calc.get_question()
        print(question)
        answer = prompt.string("Your answer: ")
        res = calc.discription()
        if int(answer) == res:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
        print(f"Congratulations, {name}!")
