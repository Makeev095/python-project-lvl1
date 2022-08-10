import prompt
from random import randint
from math import sqrt
from itertools import count, islice


def is_prime():

    name = prompt.string('May I have your name? ')
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    right_answers = 0
    while right_answers != 3:
        number = randint(1, 100)
        if number < 2:
            correct_answer = 'no'
        for number in islice(count(2), int(sqrt(number) - 1)):
            if not number % number:
                correct_answer = 'no'
        correct_answer = 'yes'

        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        result = correct_answer
        if answer == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
            right_answers = 0
            break
    print(f"Congratulations, {name}!")
