import prompt


def welcome_user():
    print("Welcome to Brain Games!")
    name = prompt.string('May i have you name? ')
    print("Hello, {}!".format(name))
    return name


def run(text):
    name = welcome_user()
    print(text)
    return name
