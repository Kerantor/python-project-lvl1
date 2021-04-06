from random import randint
import prompt


def check(name):
    n = 0
    while n < 3:
        random_number = randint(1, 100)
        print('Question: {}'.format(random_number))
        answer = prompt.string('Your answer: ')
        if (random_number % 2) == 0:
            if answer == 'yes':
                n += 1
                print('Correct!')
            else:
                print(
                    "'{}' is wrong answer ;(."
                    " Correct answer was 'yes'.\nLet's try again, {}!"
                    .format(answer, name))
                break
        elif (random_number % 2) != 0:
            if answer == 'no':
                n += 1
                print('Correct!')
            else:
                print(
                    "'{}' is wrong answer ;(."
                    " Correct answer was 'no'.\nLet's try again, {}!"
                    .format(answer, name))
            break
    return n


def brain_even():
    name = prompt.string('May i have you name? ')
    print(
        'Hello, {}!\nAnswer "yes" if the number is even, otherwise answer "no".'
        .format(name))
    n = check(name)
    if n == 3:
        print('Congratulations, {}!'.format(name))
