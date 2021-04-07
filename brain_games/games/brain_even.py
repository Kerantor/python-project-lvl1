from random import randint
from brain_games import cli
import prompt


def check_even(name):
    n = 0
    while n < 3:
        r_num = randint(1, 100)
        print('Question: {}'.format(r_num))
        answer = prompt.string('Your answer: ')
        if (r_num % 2) == 0:
            if answer == 'yes':
                n += 1
                print('Correct!')
            else:
                print(
                    "'{}' is wrong answer ;(."
                    " Correct answer was 'yes'.\nLet's try again, {}!"
                    .format(answer, name))
                break
        elif (r_num % 2) != 0:
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
    name = cli.welcome_user()
    print(
        'Answer "yes" if the number is even, otherwise answer "no".'
    )
    n = check_even(name)
    if n == 3:
        print('Congratulations, {}!'.format(name))
