from random import randint
from brain_games import cli
import prompt


def calc_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    gcd = num1 + num2
    return gcd


def brain_gcd():
    name = cli.run(
        "Find the greatest common divisor of given numbers."
    )
    n = 0
    while n < 3:
        r_num1 = randint(1, 100)
        r_num2 = randint(1, 100)
        print('Question: {} {}'.format(r_num1, r_num2))
        answer = prompt.string('Your answer: ')
        right_answer = calc_gcd(r_num1, r_num2)
        if answer == str(right_answer):
            n += 1
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(."
                " Correct answer was '{}'\nLet's try again, {}!"
                .format(answer, right_answer, name))
            break
    if n == 3:
        print('Congratulations, {}!'.format(name))
