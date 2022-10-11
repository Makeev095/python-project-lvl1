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
