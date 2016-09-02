class __Node(object):

    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class SequentialSearchST(object):

    first = None

    def get(self, key):
        x = __Node(first)
        while x! = None:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        x = __Node(first)
        while x != None:
            if key == x.key:
                x.val = val
                return
            x = x.next
        first = __Node(key, val, first)

    def contains(self, key):
        x = __Node(first)
        while x! = None:
            if key == x.key:
                return True
            x = x.next
        return False

    def keys(self):
        counter = 0
        x = __node(first)
        while x! = None:
            counter += 1
        return counter
