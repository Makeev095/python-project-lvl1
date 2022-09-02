import prompt
from random import randint
from random import choice


def calc_operations():
    name = prompt.string('May I have your name? ')
    task_1 = print("""What is the result of the expression? """)
    right_answers = 0
    while right_answers != 3:
        operand_1 = randint(1, 100)
        operand_2 = randint(1, 100)
        operation = choice('-+*')
        print(f"Question: {operand_1} {operation} {operand_2}")
        answer = prompt.string("Your answer: ")
        if operation == '+':
            result = operand_1 + operand_2

        elif operation == '-':
            result = operand_1 - operand_2

        elif operation == '*':
            result = operand_1 * operand_2
        if int(answer) == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
    return task_1, answer, name, right_answers


def calc_description():
    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operation = choice('-+*')
    question_1 = print(f"Question: {operand_1} {operation} {operand_2}")
    return operand_1, operand_2, operation, question_1


def calc_generate(operation, operand_1, operand_2):
    if operation == '+':
        result = operand_1 + operand_2

    elif operation == '-':
        result = operand_1 - operand_2

    elif operation == '*':
        result = operand_1 * operand_2
    return result