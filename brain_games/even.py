import prompt
from random import randint


def is_even():

    name = prompt.string('May I have your name? ')
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    right_answers = 0
    right_1 = 'yes'
    while right_answers != 3:
        char = randint(1, 1000)
        print(f"Question: {char}")
        otvet = prompt.string("Your answer: ")
        if char % 2 == 0 and otvet == 'yes' or char % 2 != 0 and otvet == 'no':
            right_answers += 1
            print("Correct!")

            print(f"""'{otvet}' is wrong answer ;(.\n
            Correct answer was '{right_1}'.\n
            Let's try again, {name}""")
            right_answers = 0
    print(f"Congratulations, {name}")
