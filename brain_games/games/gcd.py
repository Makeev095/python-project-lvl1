import prompt
from random import randint
import math


def find_gcd():
    name = prompt.string('May I have your name? ')
    task = print("""Find the greatest common divisor of given numbers.""")
    right_answers = 0
    while right_answers != 3:
        start = 1
        end = 100
        number_1 = randint(start, end)
        number_2 = randint(start, end)
        print(f"Question: {number_1} {number_2}")
        answer = prompt.string("Your answer: ")
        result = math.gcd(number_1, number_2)
        if int(answer) == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
    return task, answer, name, result


def gcd_logic():
    start = 1
    end = 100
    number_1 = randint(start, end)
    number_2 = randint(start, end)
    print(f"Question: {number_1} {number_2}")
