"""
Coding Counting Sort Algorithm
Question 2
"""
import csv

coins = []

with open ('money.txt','r') as f:
    for line in f:
        coins.append(int(float(line)*100))
f.close()

alist = []

for i in range(max(coins)+1):
    alist.append(0)

for j in coins:
    alist[j]+=1

sort = []

for k in range(len(alist)):
    counter = alist[k]
    while counter > 0:
        sort.append(k/100)
        counter -= 1

print(sort)

