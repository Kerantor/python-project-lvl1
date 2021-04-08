import prompt


def run(text):
    print("Welcome to Brain Games!")
    name = prompt.string('May i have you name? ')
    print("Hello, {}!".format(name))
    print(text)
    return name
