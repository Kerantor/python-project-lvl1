import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have you name? ')
    print("Hello, {}!".format(name))


def run(text):
    name = welcome_user()
    print(text)
    return name
