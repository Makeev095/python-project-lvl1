import prompt
from random import randint
from random import choice


task = """What is the result of the expression? """
operand_1 = randint(1, 100)
operand_2 = randint(1, 100)
operation = choice('-+*')
question_calc = f"Question: {operand_1} {operation} {operand_2}"


def calc_operations():
    name = prompt.string('May I have your name? ')
    print(task)
    right_answers = 0
    for right_answers in range(3):
        operand_1 = randint(1, 100)
        operand_2 = randint(1, 100)
        operation = choice('-+*')
        if operation == '+':
            result = operand_1 + operand_2

        elif operation == '-':
            result = operand_1 - operand_2

        elif operation == '*':
            result = operand_1 * operand_2

        print(question_calc)
        answer = prompt.string("Your answer: ")
        if int(answer) == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")


def calc_description():
    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operation = choice('-+*')
    if operation == '+':
        result = operand_1 + operand_2

    elif operation == '-':
        result = operand_1 - operand_2

    elif operation == '*':
        result = operand_1 * operand_2
    return result
