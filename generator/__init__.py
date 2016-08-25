#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from time import time

def getRandomNumber(min, max):
    return random.randint(min ,max)

def getRandomNumbers(min, max, length):
    result = []
    for i in range(length):
        result.append(random.randint(min, max))
    return result

def getEscRandomNumbers(min, max, length):
    return getRandomNumbers(min, max, length).sort()

def noRepeat(array):
    return list(set(array))
