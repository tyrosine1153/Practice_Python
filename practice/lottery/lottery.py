from random import *


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if not num in numbers:
            numbers.append(num)
    return numbers


def draw_winning_numbers():
    numbers = sorted(generate_numbers(6))
    numbers.append(randint(1, 45))
    return numbers


def count_matching_numbers(list_1, list_2):
    count = 0
    for l1num in list_1:
        for l2num in list_2:
            if l1num == l2num:
                count += 1
    return count


def check(numbers, winning_numbers):
    correct = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_correct = count_matching_numbers(numbers, winning_numbers[6:])

    if correct == 6:
        return 1000000000
    elif correct == 5 and bonus_correct:
        return 50000000
    elif correct == 5:
        return 1000000
    elif correct == 4:
        return 50000
    elif correct == 3:
        return 5000
    else:
        return 0
