from brain_games.games.progression import *
from brain_games.games.gcd import *
from brain_games.games.calc import *
from brain_games.games.even import *
from brain_games.games.prime import *
def name():
        name = prompt.string('May I have your name? ')
        right_answers = 0

def drive():
    name()
    question_gcd()
    prime_question()
    question_even()
    progression_question()
    calc_question()
    while right_answers != 3:

        logic_gcd()
        prime_logic()
        even_logic()
        progression_logic()
        calc_logic()

        if int(answer) == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
    Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
