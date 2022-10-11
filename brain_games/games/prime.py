from random import randint


def discription():

    for _ in range(3):
        number = randint(1, 100)
        d = 2
        while number % d != 0:
            d += 1
        if d == number:
            res = 'yes'
        else:
            res = 'no'

        question_for_user = f"Question: {number}"

        return res, question_for_user


def getting_answer():

    answer = (input("Your answer: "))

    return answer


def game_question():

    question = """Answer "yes" if given number is prime. \
Otherwise answer "no"."""

    return question
