"""
Bubble Sorting Algorithm:
swaps elements if elem1>elem2
"""
def sort(lst):
    n = len(lst)
    swap = True
    while swap:
        swap = False
        for i in range(n-1):
            if lst[i]>lst[i+1]:
                swap = True
                lst[i],lst[i+1] = lst[i+1],lst[i]
    print(lst)
        
                
sort([3,2,1,5,3,5])
