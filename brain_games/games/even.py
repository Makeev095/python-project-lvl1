from random import randint


def discription():

    for _ in range(3):
        char = randint(1, 1000)
        question_for_user = f"Question: {char}"
        if char % 2 == 0:
            res = 'yes'
        elif char % 2 != 0:
            res = 'no'

        return res, question_for_user


def getting_answer():

    answer = (input("Your answer: "))

    return answer


def game_question():

    question = """Answer "yes" if the number is even, \
otherwise answer "no"."""

    return question
