"""
Stack practice
"""

class ListNode:
    def __init__(self, value):
        self._value = value
        self._link = None
    def __str__(self): return self._value
    def newlink(self, other): self._link = other
    def value(self): return self._value
    def link(self): return self._link

class Stack:
    def __init__(self):
        self._top = None
        self._length = 0

    def top(self): return self._top
    def __len__(self): return self._length

    def empty(self):
        return self._top == None

    def push(self, val):
        """
        add new item to the top of the stack
        """
        newNode = ListNode(val)
        p = self._top
        self._top = newNode
        newNode.newlink(p)

    def pop(self):
        """
        remove the top value of stack and return it
        """
        if self._top == None: return None
        p = self._top
        self._top = p.link()
        return p

    def peek(self):
        """
        return the value of the first node
        """
        return self._top

    def __str__(self):
        s = ""
        n = self._top

        while (n!= None):
            if n.link() != None:
                if type(n.value()) == str:
                    s += "'" + str(n.value()) + ",'"
                else:
                    s += str(n.value()) + ","

            else:
                s += str(n.value())

            n = n.link()

        return ("["+s+"]")

s = Stack()
print(s.empty())
s.push('a')
s.push('n')
s.pop()
print(s)
    
