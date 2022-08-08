import prompt
from random import randint


def is_prime():

    name = prompt.string('May I have your name? ')
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    right_answers = 0
    while right_answers != 3:
        number = randint(1, 100)
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5 + 1)):
            if number % i == 0:
                correct_answer = 'no'
            else:
                correct_answer = 'yes'
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        result = correct_answer
        if answer == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.\n
            Correct answer was '{result}'.\n
            Let's try again, {name}""")
            right_answers = 0
    print(f"Congratulations, {name}")