from random import randint, choice
from operator import add, sub, mul
import prompt


def check_calc(name):
    n = 0
    while n < 3:
        ran_num_1 = randint(1, 10)
        ran_num_2 = randint(1, 10)
        operation = {
            '{} + {}'.format(ran_num_1, ran_num_2): add(ran_num_1, ran_num_2),
            '{} - {}'.format(ran_num_1, ran_num_2): sub(ran_num_1, ran_num_2),
            '{} * {}'.format(ran_num_1, ran_num_2): mul(ran_num_1, ran_num_2),
        }
        r = choice(list(operation.keys()))
        print('Question: {}'.format(r))
        answer = prompt.string('Your answer: ')
        if answer == str(operation[r]):
            n += 1
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(."
                " Correct answer was {}\nLet's try again, {}!"
                .format(answer, str(operation[r]), name))
            break
    return n


def brain_calc():
    name = prompt.string('May i have you name? ')
    print(
        'Hello, {}!\nWhat is the result of the Expression?'
        .format(name))
    n = check_calc(name)
    if n == 3:
        print('Congratulations, {}!'.format(name))
