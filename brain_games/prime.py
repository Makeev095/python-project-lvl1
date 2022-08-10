import prompt
from random import randint


def is_prime():

    name = prompt.string('May I have your name? ')
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    right_answers = 0
    while right_answers != 3:
        number = randint(1, 100)
        if number==2 or number==3:
            correct_answer = 'yes'
        if number%2==0 or number<2:
            correct_answer = 'no'
        for i in range(3, int(number**0.5)+1, 2):
            if number%i==0:
                correct_answer = 'no'

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
        return 0
    print(f"Congratulations, {name}!")