#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Algorithms Pracitice: ThreeSum question
A program with cubic running time. Reads n integers and counts the number of
triples that sum to exactly 0 (Intergers are different in this array)
算法训练： 三元和的问题
统计所有和为 0 的三整数元组的数量（数组内整数均不相等）
"""

import sys
sys.path.append('../')

from BinarySearch import BinarySearch
from generator import *

class ThreeSum(object):

    @staticmethod
    def count(input):
        start = time()
        cnt = 0
        result = []

        for i in range(len(input)):
            for j in range(i+1, len(input)):
                for k in range(j+1, len(input)):
                    if input[i] + input[j] + input[k] == 0:
                        result.append([input[i], input[j], input[k]])
                        cnt += 1
        end = time()
        print('time: %s, count: %d' % (end - start, cnt))

    @staticmethod
    def countFast(input):
        start = time()
        cnt = 0
        result = []
        input.sort()

        for i in range(len(input)):
            for j in range(i+1, len(input)):
                if BinarySearch(input, -input[i]-input[j]) > j:
                    result.append([input[i], input[j], -input[i]-input[j]])
                    cnt += 1
        end = time()
        print('time: %s, count: %d' % (end - start, cnt))


class TwoSum(object):

    @staticmethod
    def count(input):

        start = time()
        cnt = 0
        result = []

        for i in range(len(input)):
            for j in range(i+1, len(input)):
                if input[i] + input[j] == 0:
                    result.append([input[i], input[j]])
                    cnt += 1
        end = time()
        print('time: %s, count: %d' % (end - start, cnt))

    @staticmethod
    def countFast(input):
        start = time()
        cnt = 0
        result = []
        input.sort()

        for i in range(len(input)):
            if BinarySearch(input, -input[i]) > i:
                result.append([input[i], -input[i]])
                cnt += 1
        end = time()
        print('time: %s, count: %d' % (end - start, cnt))

data = noRepeat(getRandomNumbers(-1000, 1000, 100))

TwoSum.count(data)
TwoSum.countFast(data)
ThreeSum.count(data)
ThreeSum.countFast(data)
