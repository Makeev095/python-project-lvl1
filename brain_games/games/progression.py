from random import randint


QUESTION = "What number is missing in the progression? "

answer_type = int


def generate_round():

    num1 = randint(1, 10)
    num2 = randint(80, 100)
    n = randint(2, 10)
    progression = []
    progression = list(range(num1, num2, n))
    index = randint(1, len(progression) - 1)
    res = progression[index]
    progression[index] = '..'
    new_progression = (' '.join(map(str, progression)))

    question_info = new_progression

    return res, question_info
