from math import *
l1 = [1,2,3,4,5,6,7,8]
l = len(l1)
min = l1[0]
for i in range(l):
    if l1[i] < min:
        min = l1[i]
print("The minimum value is :",min)

#max value
l  = [1,2,3,333,55,66,66,55,5453]
s = len(l)
max =  l[0]
for i in range(s):
    if l[i] > min:
        max = l[i]
print("The maximum value is",max)

lst = []
n = int(input("Enter number of element you wanted to enter : "))
for i in range(n):
    no = int(input("Enter the element you wanted to enter : "))
    lst.append(no)

print(lst)
r = len(lst)
min = len(lst)
for i in range(r):
    if lst[i] < min:
        min = lst[i]

print("The minimum value is",min)
