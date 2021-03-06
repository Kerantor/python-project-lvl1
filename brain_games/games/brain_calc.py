from random import randint, choice
from operator import add, sub, mul
from brain_games import cli
import prompt


def brain_calc():
    name = cli.run(
        "What is the result of the Expression?"
    )
    n = 0
    while n < 3:
        r_num1 = randint(1, 10)
        r_num2 = randint(1, 10)
        operation = {
            '{} + {}'.format(r_num1, r_num2): add(r_num1, r_num2),
            '{} - {}'.format(r_num1, r_num2): sub(r_num1, r_num2),
            '{} * {}'.format(r_num1, r_num2): mul(r_num1, r_num2),
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
                " Correct answer was '{}'\nLet's try again, {}!"
                .format(answer, operation[r], name))
            break
    if n == 3:
        print('Congratulations, {}!'.format(name))
