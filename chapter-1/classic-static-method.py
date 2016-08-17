# count a interger absolute value

def abs(x):
    if x < 0:
        return -x
    else:
        return x

# judge a number is prime

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            if i * i >= n:
                break
        return True

# count hypotenuse in triangle

def hypotenuse(a, b):
    return Math.sqrt(a*a + b*b)
