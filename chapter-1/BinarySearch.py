
def BinarySearch(input, key):
    lo = 0
    hi = len(input) - 1
    while(lo <= hi):
        mid = int(lo + (hi-lo) / 2)
        if (key < input[mid]):
            hi = mid - 1
        elif (key > input[mid]):
            lo = mid + 1
        else:
            return mid
    return -1

a = [1, 4, 5, 6, 11, 15, 20, 30, 31, 35]

print(BinarySearch(a, 32))
