"""
Queue
"""
class ListNode:
    def __init__(self, value):
        self._value = value
        self._link = None

    def __str__(self): return self._value
    def value(self): return self._value

    def link(self): return self._link
    def newlink(self, other): self._link = other

class Queue:
    """
    head tail
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def insert(self, value):
        """insert into tail"""
        newNode = ListNode(value)

        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.newlink(newNode)
            self._tail = newNode
        self._length += 1

    def remove(self):
        """remove the head"""
        if self._head == None:
            return None
        e = self._head
        self._head = self._head.link()
        self._length -= 1
        return e
    def __str__(self):
        n = self._head
        s = ""


        while (n!=None):
            if n.link() != None:
                if type(n.value()) == str:
                    s += "'" + str(n.value()) + "',"
                else:
                    s += str(n.value()) + ","

            else:
                s += "'"+str(n.value()) + "'"

            n = n.link()
        return ("["+s+"]")

    def empty(self): return self._head == None

    def peek(self): return self._head
    
def main():
    q = Queue()
    print(q.empty())
    q.insert('a')
    q.insert('b')
    q.insert('c')
    q.remove()
    print(q.peek())

if __name__ == '__main__': main()

