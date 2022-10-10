import prompt
from random import randint


def discription():

    for _ in range(3):
        num1 = randint(1, 10)
        num2 = randint(80, 100)
        n = randint(2, 10)
        progression = []
        progression = list(range(num1, num2, n))
        index = randint(1, len(progression) - 1)
        res = progression[index]
        progression[index] = '..'
        new_progression = (' '.join(map(str, progression)))

        question_for_user = f"Question: {new_progression}"

        return res, question_for_user


def getting_answer():

    answer = int(input("Your answer: "))
    answer = int(answer)

    return answer


def game_question():

    question = "What number is missing in the progression? "

    return question


def find_progression():

    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("What number is missing in the progression? ")
    right_answers = 0
    while right_answers != 3:
        num1 = randint(1, 10)
        num2 = randint(80, 100)
        n = randint(2, 10)
        progression = []
        progression = list(range(num1, num2, n))
        index = randint(1, len(progression) - 1)
        correct_answer = progression[index]
        progression[index] = '..'
        new_progression = (' '.join(map(str, progression)))

        print(f"Question: {new_progression}")
        answer = prompt.string("Your answer: ")
        res = correct_answer

        if int(answer) == res:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")


def get_question():
    question = "What number is missing in the progression?"
    return question
