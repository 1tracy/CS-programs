"""
Create recursive method that returns the index
of an item in a list.
"""
def index(item, lst):
    if lst[0] == item:
        return 0
    else:
        return 1+index(item, lst[1:])

a = index(2, [1,3,5,3,4,5,6,2])
print(a)
