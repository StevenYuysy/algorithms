#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from time import time


def getRandomNumber(min, max):

    """Product one random number between `min` and `max`.

    Args:
        min: The minimum number
        max: The maximum number

    Returns:
        An interger. For example: 5
    """

    return random.randint(min ,max)

def getRandomNumbers(min, max, length):

    """Product `amount` random numbers between `min` and `max`.

    Args:
        min: The minimum number
        max: The maximum number
        length: The amount number

    Returns:
        An array. For example: [1, 2, 1, 5, 6, 10, 21, 50, 31]
    """

    result = []
    for i in range(length):
        result.append(random.randint(min, max))
    return result

def getEscRandomNumbers(min, max, length):

    """Product `amount` random numbers between `min` and `max`, list at esc order.

    Args:
        min: The minimum number
        max: The maximum number
        length: The amount number

    Returns:
        An array. For example: [1, 2, 5, 6, 10, 21, 31]
    """

    return getRandomNumbers(min, max, length).sort()

def noRepeat(array):

    """Get no-repeat data.

    Args:
        array: An array that need to get no-repeat data.

    Returns:
        An array. For example: [1, 2, 5, 6, 10, 21, 31]
    """

    return list(set(array))
