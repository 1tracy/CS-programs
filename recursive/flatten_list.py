"""
Create a recursive method that flattens a list and returns a string
of all the elements in the list.
If any of the list items are lists themselves their contents
are retrieved from those nested lists.
"""
def flatten(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        #check if lst[0] is nested

a = flatten([1, 2, 3])
print(a)

