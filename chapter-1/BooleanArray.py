# boolean array practice

def getGCD(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return True if a == 1 else False

def createArray(N):
    table= [ [ 0 for i in range(N) ] for j in range(N) ]
    for i in range(N):
        for j in range(N):
            table[i][j] = getGCD(i ,j)
    return table

print (createArray(6))
