import prompt
from random import randint
from random import choice


operand_1 = randint(1, 100)
operand_2 = randint(1, 100)
operation = choice('-+*')

def discription():

    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operation = choice('-+*')
    if operation == '+':
        res = operand_1 + operand_2

    elif operation == '-':
        res = operand_1 - operand_2

    elif operation == '*':
        res = operand_1 * operand_2

    return res


def question_game():
    question = """What is the result of the expression? """
    return question


def give_question():
    question_for_user = f"Question: {operand_1} {operation} {operand_2}"

    return question_for_user


def calc_operations():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("""What is the result of the expression? """)
    right_answers = 0
    for right_answers in range(3):
        operand_1 = randint(1, 100)
        operand_2 = randint(1, 100)
        operation = choice('-+*')
        if operation == '+':
            res = operand_1 + operand_2

        elif operation == '-':
            res = operand_1 - operand_2

        elif operation == '*':
            res = operand_1 * operand_2

        problem = f"Question: {operand_1} {operation} {operand_2}"
        print(problem)
        answer = prompt.string("Your answer: ")
        if int(answer) == res:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
