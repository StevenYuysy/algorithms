class Node(object):

    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class SequentialSearchST(object):

    def __init__(self):
        self.__first = None

    def get(self, key):
        x = self.__first
        while x != None:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        x = self.__first
        while x != None:
            if key == x.key:
                x.val = val
                return
            x = x.next
        self.__first = Node(key, val, self.__first)

    def contains(self, key):
        x = self.__first
        while x != None:
            if key == x.key:
                return True
            x = x.next
        return False

    def keys(self):
        array = []
        x = self.__first
        while x != None:
            array.append(x.key)
            x = x.next
        array.reverse()
        return array 
