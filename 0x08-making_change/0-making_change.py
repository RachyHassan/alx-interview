#!/usr/bin/python3
"""
    Making Change
"""


def makeChange(coins, total):
    """
    Makes change

    Args:
    - coins: list of integers greater than 0.
    - total: integer

    Return: fewest number of coins needed to meet total
    """

    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    possible_answers = []

    for j in range(0, len(coins)):
        count = 0
        diff = 9999999
        for i in range(j, len(coins)):
            while diff >= coins[i] and diff > 0:
                if diff == 9999999:
                    diff = total - coins[i]
                else:
                    diff = diff - coins[i]
                count += 1
        if diff != 0:
            count = 0
        possible_answers.append(count)

    answers = [i for i in possible_answers if i != 0]
    if answers == []:
        return -1
    return min(answers)
