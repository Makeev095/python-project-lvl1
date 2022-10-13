import prompt


def run(game):
    ROUNDS = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    for _ in range(ROUNDS):
        res, question_info = game.generate_round()
        question = game.QUESTION
        print(question)
        print((f"Question: {question_info}"))
        answer = game.answer_type(input("Your answer: "))
        if answer == res:
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{res}'.
Let's try again, {name}!""")
            return 0
    print(f"Congratulations, {name}!")
