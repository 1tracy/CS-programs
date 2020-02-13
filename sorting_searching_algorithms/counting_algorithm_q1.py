"""
Coding Counting Sort Algorithm
Question 1, Scenario 1
Sorting Negative Integers
"""
def counted_negative(lst):

    minIndex = 0
    maxIndex = 0
    for i in range(len(lst)):
        if lst[minIndex] > lst[i]:
            minIndex = i
        if lst[maxIndex] < lst[i]:
            maxIndex = i

    number_of_keys = abs(lst[minIndex]) + lst[maxIndex]

    LIST = []
    for j in range(number_of_keys+1):
        LIST.append(0)
        
    offset_value = abs(lst[minIndex])
    for number in lst:
        LIST[number+offset_value] += 1

    sortedList = []
    for k in range(0, len(LIST)):
        counter = LIST[k]
        while counter > 0:
            sortedList.append(k-offset_value)
            counter -= 1
    return sortedList


#lst = [19,20,21,22,23,34,45]
#aList = counted_negative(lst)
#print (aList)

"""
Question 1, Scenario 2
Dramatic Offset Value Optimization
"""
def counted_offset(lst):
    minIndex = 0
    maxIndex = 0
    
    for i in lst:
        if lst[minIndex] > i:
            minIndex = lst.index(i)
        if lst[maxIndex] < i:
            maxIndex = lst.index(i)
            
    offset = abs(lst[minIndex])
    number_of_keys = lst[maxIndex]-lst[minIndex]
    
    alist = []
    for j in range(number_of_keys+1):
        alist.append(0)
    print(alist)
    
    for k in lst:
        alist[k-offset]+=1

    sortedList = []
    for m in range(0, len(alist)):
        counter = alist[m]
        while counter > 0:
            sortedList.append(m+offset)
            counter -= 1

    return sortedList

lst = [19,20,18,20,13,20]
lists = counted_offset(lst)
print (lists)
