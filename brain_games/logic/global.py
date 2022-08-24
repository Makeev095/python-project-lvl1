from brain_games.games.gcd import info_gcd, gcd_question
from brain_games.games.cli import welcome_user, get_answer
from brain_games.games.calc import calc_question, calc_info
from brain_games.games.progression import progression_info, progression_question
from brain_games.games.even import even_info, even_question
from brain_games.games.prime import prime_info, prime_question


def drive(right_answers):
    welcome_user
    gcd_question
    calc_question
    even_question
    progression_question
    prime_question
    right_answers = 0
    while right_answers != 3:
        answer_check


def answer_check(answer, result, name, right_answers):
    info_gcd
    calc_info
    even_info
    progression_info
    prime_info
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
