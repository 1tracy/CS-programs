"""
Bubble Sort
swap decreasing
"""
def sort(lst):
    for i in range(len(lst)):
        mini = i
        for j in range(i+1, len(lst)):
            if lst[mini]>lst[j]:
                mini= j
        lst[mini],lst[i] = lst[i],lst[mini]

    return lst
        

lst = [2,4,6,2,4,56,2,5]
aa = sort(lst)
print(aa)
