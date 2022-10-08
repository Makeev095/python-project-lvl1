import prompt
from brain_games.games import calc


def run(game):
    game = calc
    right_answers = 0
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    while right_answers < 3:
        operand_1, operation, operand_2, res = game.calc_operations()
        print(game.question_game())
        result = calc.give_question(operand_1, operation, operand_2)
        print(result)
        answer = prompt.string("Your answer: ")
        if int(answer) == res:
            print("Correct!")
            right_answers += 1
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")
