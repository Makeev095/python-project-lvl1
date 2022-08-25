from brain_games.games.calc import calc_info
from brain_games.games.cli import welcome_user
from brain_games.games.even import even_info
from brain_games.games.gcd import gcd_logic
from brain_games.games.progression import progression_info
from brain_games.games.prime import prime_info


def drive(task, answer, name, result):
    welcome_user
    print(name)
    print(task)
    right_answers = 0
    while right_answers != 3:
        gcd_logic
        prime_info
        progression_info
        calc_info
        even_info
    if int(answer) == result:
        right_answers += 1
        print("Correct!")
    else:
        print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
        right_answers = 0
        return 0
    print(f"Congratulations, {name}!")
