from random import randint
import math


QUESTION = """Find the greatest common divisor of given numbers."""

answer_type = int


def generate_round():

    start = 1
    end = 100
    number_1 = randint(start, end)
    number_2 = randint(start, end)
    res = math.gcd(number_1, number_2)
    question_info = f"{number_1} {number_2}"

    return res, question_info
