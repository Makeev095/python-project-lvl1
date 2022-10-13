from random import randint


QUESTION = """Answer "yes" if the number is even, \
otherwise answer "no"."""

answer_type = str


def generate_round():

    char = randint(1, 1000)
    question_info = char
    if char % 2 == 0:
        res = 'yes'
    elif char % 2 != 0:
        res = 'no'

    return res, question_info
