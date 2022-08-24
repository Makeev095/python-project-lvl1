import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


def get_answer():
    answer = prompt.string("Your answer: ")
    return answer
