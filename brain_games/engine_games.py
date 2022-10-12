import prompt


def run(game):
    rounds = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    question = game.game_question()
    print(question)
    for _ in range(rounds):
        res, result = game.discription()
        print(result)
        answer = game.getting_answer()
        if answer == res:
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            return 0
    print(f"Congratulations, {name}!")
