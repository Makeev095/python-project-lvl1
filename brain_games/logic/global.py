from brain_games.games.gcd import info_gcd
from brain_games.games.cli import welcome_user, get_answer


def gcd_question():
    print("""Find the greatest common divisor of given numbers.""")
    right_answers = 0
    return right_answers


def drive(right_answers):
    welcome_user
    gcd_question
    right_answers
    while right_answers != 3:
        answer_check


def answer_check(answer, result, name, right_answers):
    info_gcd
    get_answer
    if int(answer) == result:
        right_answers += 1
        print("Correct!")
    else:
        print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
        right_answers = 0
        return 0
    print(f"Congratulations, {name}!")
