import prompt
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


def game_question():

    question = """Answer "yes" if the number is even, \
otherwise answer "no"."""

    return question


def is_even():

    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("""Answer "yes" if the number is even, \
otherwise answer "no".""")
    right_answers = 0
    while right_answers != 3:
        char = randint(1, 1000)
        print(f"Question: {char}")
        answer = prompt.string("Your answer: ")
        if char % 2 == 0:
            res = 'yes'
        elif char % 2 != 0:
            res = 'no'
        if answer == res:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
