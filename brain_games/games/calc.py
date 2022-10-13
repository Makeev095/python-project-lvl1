from random import randint
from random import choice


QUESTION = """What is the result of the expression? """

answer_type = int


def generate_round():

    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operation = choice('-+*')
    if operation == '+':
        res = operand_1 + operand_2

    elif operation == '-':
        res = operand_1 - operand_2

    elif operation == '*':
        res = operand_1 * operand_2

    question_info = f"{operand_1} {operation} {operand_2}"

    return res, question_info
