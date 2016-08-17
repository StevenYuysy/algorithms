import math

class Stack:
    ''' a Stack Class'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# only support Interger

def Evaluate(input):
    ops = Stack()
    vals = Stack()

    for s in input.split(' '):
        if s == '+' \
        or s == '-' \
        or s == '*' \
        or s == '/' \
        or s == 'sqrt':
            ops.push(s)

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
            vals.push(v)

        else:
            vals.push(int(s))

    print(vals.pop())


Evaluate('( 5 - ( 1 + 1 ) )')
Evaluate('( 1 + ( ( 2 + 3 ) * ( 4 + 5 ) ) )')
Evaluate('( ( 1 + sqrt ( 5 ) ) / 2 )')
