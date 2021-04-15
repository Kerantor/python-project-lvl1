import prompt


def welcome_user():
    print("Welcome to Brain Games!")


def run(text):
    welcome_user()
    name = prompt.string('May i have you name? ')
    print("Hello, {}!".format(name))
    print(text)
    return name
