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
