from random import randint
from brain_games import cli
import prompt


def check_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def brain_even():
    name = cli.run(
        "Answer 'yes' if the number is even, otherwise answer 'no'."
    )
    n = 0
    while n < 3:
        r_num = randint(1, 100)
        print('Question: {}'.format(r_num))
        user_answer = prompt.string('Your answer: ')
        right_answer = check_even(r_num)
        if user_answer == right_answer:
            n += 1
            print('Correct!')
        else:
            if right_answer == 'yes':
                print(
                    "'{}' is wrong answer ;(."
                    " Correct answer was 'yes'.\nLet's try again, {}!"
                    .format(user_answer, name))
                break
            else:
                print(
                    "'{}' is wrong answer ;(."
                    " Correct answer was 'no'.\nLet's try again, {}!"
                    .format(user_answer, name))
            break
    if n == 3:
        print('Congratulations, {}!'.format(name))
