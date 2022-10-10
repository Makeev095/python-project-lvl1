import prompt
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


def is_prime():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    right_answers = 0
    while right_answers != 3:
        number = randint(1, 100)
        d = 2
        while number % d != 0:
            d += 1
        if d == number:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        res = correct_answer
        if answer == res:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.)
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")


def get_question():
    quest = """Answer "yes" if given number is prime. Otherwise answer "no"."""
    return quest
