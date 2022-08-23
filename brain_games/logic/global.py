from brain_games.games.progression import *
from brain_games.games.gcd import info_gcd, question_gcdd
from brain_games.games.calc import *
from brain_games.games.even import *
from brain_games.games.prime import *

def name_get():
    name = prompt.string('May I have your name? ')

def drive():
    name = prompt.string('May I have your name? ')
    question_gcdd
    right_answers = 0
    while right_answers != 3:
        info_gcd
        answer_check

def answer_check():
    if int(answer) == result:
            right_answers += 1
            print("Correct!")
    else:
        print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
        right_answers = 0
        return 0
    print(f"Congratulations, {name}!")