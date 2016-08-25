#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from time import time

def getRandomNumber(min, max):
    return int(random.randint(min ,max))

def getRandomNumbers(min, max, length):
    result = []
    for i in range(length):
        result.append(random.randint(min, max))
    return result

def getEscRandomNumbers(min, max, length):
    result = getRandomNumbers(min, max, length)
    result.sort()
    return result

def noRepeat(array):
    return list(set(array))
