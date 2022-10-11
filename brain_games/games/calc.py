from random import randint
from random import choice


def discription():
    for _ in range(3):
        operand_1 = randint(1, 100)
        operand_2 = randint(1, 100)
        operation = choice('-+*')
        if operation == '+':
            res = operand_1 + operand_2

        elif operation == '-':
            res = operand_1 - operand_2

        elif operation == '*':
            res = operand_1 * operand_2

        question_for_user = f"Question: {operand_1} {operation} {operand_2}"

        return res, question_for_user


def getting_answer():

    answer = int(input("Your answer: "))
    answer = int(answer)

    return answer


def game_question():
    question = """What is the result of the expression? """
    return question
