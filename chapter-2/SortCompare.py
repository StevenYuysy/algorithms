#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from generator import *
from Insertion import insertion
from Selection import selection
from Shell import shell

input = getRandomNumbers(0, 100000, 10000)

def counter(function):
    start = time()
    function(input)
    end = time()
    return end-start

print 'SortType: insertion, Time: %s' % counter(insertion)
print 'SortType: selection, Time: %s' % counter(selection)
print 'SortType: shell, Time: %s' % counter(shell)
