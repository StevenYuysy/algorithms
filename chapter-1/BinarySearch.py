# A very claasic BinarySearch

def BinarySearch(input, key):
    lo = 0
    hi = len(input) - 1
    while lo <= hi:
        mid = int(lo + (hi-lo) / 2)
        if key < input[mid]:
            hi = mid - 1
        elif key > input[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":

    import sys
    sys.path.append('../')

    from generator import *

    input = getEscRandomNumbers(0, 10000, 10)
    index = getRandomNumber(0, 9)
    print 'find key: %s index: %d in %s' % (input[index], index, input)
    print BinarySearch(input, input[index])
