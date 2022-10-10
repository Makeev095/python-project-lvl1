import prompt
from random import randint
import math


def discription():

    for _ in range(3):
        start = 1
        end = 100
        number_1 = randint(start, end)
        number_2 = randint(start, end)
        res = math.gcd(number_1, number_2)
        question_for_user = f"Question: {number_1} {number_2}"
        

        return res, question_for_user


def getting_answer():

    answer = int(input("Your answer: "))
    answer = int(answer)

    return answer


def game_question():

    question = """Find the greatest common divisor of given numbers."""

    return question


def find_gcd():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("""Find the greatest common divisor of given numbers.""")
    right_answers = 0
    while right_answers != 3:
        start = 1
        end = 100
        number_1 = randint(start, end)
        number_2 = randint(start, end)
        print(f"Question: {number_1} {number_2}")
        res = math.gcd(number_1, number_2)
        answer = prompt.string("Your answer: ")
        if int(answer) == res:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
