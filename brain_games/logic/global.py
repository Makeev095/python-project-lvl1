from brain_games.games.progression import *
from brain_games.games.gcd import result_getting_gcd, question_gcd, logic_gcd
from brain_games.games.calc import *
from brain_games.games.even import *
from brain_games.games.prime import *
import math

start = 1
end = 100
answer = prompt.string("Your answer: ")
result = math.gcd(start, end)
name = prompt.string('May I have your name? ')

def name_question():

    name = prompt.string('May I have your name? ')

def answer_getting():

    answer = prompt.string("Your answer: ")

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

def drive():
    name_question()
    question_gcd()
    right_answers = 0
    while right_answers != 3:
        logic_gcd
        answer = prompt.string("Your answer: ")
        result_getting_gcd
        answer_check
