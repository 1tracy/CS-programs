"""
radix sort
"""
import math
from testingqueue import *

"""
1. calculate length of longest digit
2. generate a list of 10 queues to hold numbers
3. outside loop runs # of digits in longest num
4. extract particular digit being sorted
5. put number in appropriate queue
6. dequeue the queues
"""

def radixSort(alist):
    #1
    longest = len(str(max(alist)))
    #2
    queuelist = []
    for i in range(10):
        i = Queue()
        queuelist.append(i)
    #3
    for i in range(longest):
        for n in alist:
            index = (n//10 ** i) % 10

            newnode = ListNode(n)

            queuelist[index].insert(newnode)

        for x in queuelist:
            for i in x: print(i.value())
            print(x.value())





lst = [2,5,33,12,656,434,343,24,6]
radixSort(lst)
