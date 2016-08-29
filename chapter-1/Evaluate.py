import math

def Evaluate(input):
    ops = []
    vals = []

    for s in input.split(' '):
        if s == '+' \
        or s == '-' \
        or s == '*' \
        or s == '/' \
        or s == 'sqrt':
            ops.append(s)

        elif s == '(':
            continue

        elif s == ')':
            op = ops.pop()
            v = vals.pop()
            if op == '+':
                v = vals.pop() + v
            elif op == '-':
                v = vals.pop() - v
            elif op == '*':
                v = vals.pop() * v
            elif op == '/':
                v = vals.pop() / v
            elif op == 'sqrt':
                v = math.sqrt(v)
            vals.append(v)

        else:
            vals.append(int(s))

    print(vals.pop())

if __name__ == "__main__":

    Evaluate('( 5 - ( 1 + 1 ) )')
    Evaluate('( 1 + ( ( 2 + 3 ) * ( 4 + 5 ) ) )')
    Evaluate('( ( 1 + sqrt ( 5 ) ) / 2 )')
