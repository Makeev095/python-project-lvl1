from random import randint


QUESTION = """Answer "yes" if given number is prime. \
Otherwise answer "no"."""

answer_type = str


def generate_round():

    number = randint(1, 100)
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        res = 'yes'
    else:
        res = 'no'

    question_info = number

    return res, question_info
