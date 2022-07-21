import prompt
from random import randint

def is_even():
    name = prompt.string('May I have your name? ')
    print(f"""Answer "yes" if the number is even, otherwise answer "no".""")
    right_answers = 0
    right_1 = 'yes'
    right_2 = 'no'
    while right_answers !=3:
        random_char = randint(1,1000)
        print(f"Question: {random_char}")
        answer = prompt.string("Your answer: ")
        if random_char % 2 == 0 and answer == 'yes' or random_char % 2 != 0 and answer == 'no':
            right_answers += 1
            print("Correct!")
        else: 
            print(f"""'{answer}' is wrong answer ;(.\n Correct answer was '{right_1}'.\n Let's try again, {name}""")
            right_answers = 0
    print(f"Congratulations, {name}")




