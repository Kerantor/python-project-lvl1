import prompt


def welcome_user():
    print("Welcome to Brain Games!")
    name = prompt.string('May i have you name? ')
    print("Hello, {}!".format(name))
    return name
