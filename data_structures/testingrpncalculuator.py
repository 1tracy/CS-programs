"""
RPN calculator
Stack
"""

class ListNode:
    def __init__(self, value):
        self._value = value
        self._link = None

    def newlink(self, node): self._link = node
    def link(self): return self._link
    def value(self): return self._value
    def __str__(self): return self._value

class Stack:
    def __init__(self):
        self._head = None
        self._length = 0

    def __len__(self): return self._length
    def head(self): return self._head
    def peek(self): return self._head
    def empty(self): return (self._head == None)
    def push(self, value):
        newnode = ListNode(value)
        p = self._head
        self._head = newnode
        newnode.newlink(p)
        self._length += 1
    def pop(self):
        p = self._head
        if p == None: return None
        self._head = self._head.link()
        return p
    def __str__(self):
        s = ""
        n = self._head

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
    
def calculator(lst):
    s = Stack()
    for i in lst:
        if i.isdigit():
            s.push(int(i))
        else:
            n1 = s.pop().value()
            n2 = s.pop().value()
            
            if i == '-':
                n3 = n1 - n2
            elif i == '+':
                n3 = n1 + n2
            elif i == 'x' or i == '*':
                n3 = n1 * n2
            else:
                n3 = n1 / n2
            s.push(n3)
    answer = s.pop().value()
    print(answer)
    print(s.empty())
    
calculator(['1','2','3','4','x','-','+'])

    
