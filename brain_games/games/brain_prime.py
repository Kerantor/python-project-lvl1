from random import randint
from brain_games import cli
import prompt


def is_even(num):
    if num % 2 == 0:
        return 'no'
    d = 3
    while d * d < num and num % d != 0:
        d += 2
    if d * d > num:
        return 'yes'
    return 'no'


def brain_prime():
    name = cli.run(
        "Answer 'yes' if given number is prime. Otherwise answer 'no'."
    )
    n = 0
    while n < 3:
        r_num1 = randint(1, 100)
        print('Question: {}'.format(r_num1))
        user_answer = prompt.string('Your answer: ')
        right_answer = is_even(r_num1)
        if user_answer == str(right_answer):
            n += 1
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(."
                " Correct answer was '{}'.\nLet's try again, {}!"
                .format(user_answer, right_answer, name))
            break
    if n == 3:
        print('Congratulations, {}!'.format(name))
