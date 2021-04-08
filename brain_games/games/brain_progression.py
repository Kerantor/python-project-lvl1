from random import randint, choice
from brain_games import cli
import prompt


def brain_progression():
    name = cli.run(
        "What number is missing in the progression?"
    )
    n = 0
    while n < 3:
        num_list = []
        r_num1 = randint(1, 10)
        delta = randint(1, 10)
        list_range = randint(5, 10)
        i = 0
        while i < list_range:
            num_list.append(r_num1)
            r_num1 += delta
            i += 1
        right_num = choice(num_list)
        num_index = num_list.index(right_num)
        print_list = num_list.copy()
        print_list[num_index] = '..'
        print_list = ' '.join(str(e) for e in print_list)
        print('Question: {}'.format(print_list))
        answer = prompt.string('Your answer: ')
        if answer == str(right_num):
            n += 1
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(."
                " Correct answer was '{}'\nLet's try again, {}!"
                .format(answer, right_num, name))
            break
    if n == 3:
        print('Congratulations, {}!'.format(name))
