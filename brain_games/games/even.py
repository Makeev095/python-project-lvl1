import prompt
from random import randint


def is_even():

    name = prompt.string('May I have your name? ')
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    right_answers = 0
    while right_answers != 3:
        char = randint(1, 1000)
        print(f"Question: {char}")
        answer = prompt.string("Your answer: ")
        answer = answer
        if char % 2 == 0:
            result = 'yes'
        elif char % 2 != 0:
            result = 'no'
        if answer == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
