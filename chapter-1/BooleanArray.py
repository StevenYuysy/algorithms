"""
Write a program, creating a boolean array[][] which is N x N. If i and j are
coprime, a[i][j] is equal to True, else is equal to Fals.
"""

def createArray(N):

    def getGCD(a, b):
        if a < b:
            a, b = b, a

        while b != 0:
            temp = a % b
            a = b
            b = temp

        return True if a == 1 else False


    table= [ [ 0 for i in range(N) ] for j in range(N) ]
    for i in range(N):
        for j in range(N):
            table[i][j] = getGCD(i ,j)
    return table

if __name__ == "__main__":

    N = input('size --> ')
    print(createArray(int(N)))
