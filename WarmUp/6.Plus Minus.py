#!/bin/python3

import sys
(p,n1,z)=(0,0,0)

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(n):
    if(arr[i]>0):
        p=p+1
    elif(arr[i]<0):
        n1=n1+1
    else:
        z=z+1
print(format(p/n,',.6f'))
print(format(n1/n,',.6f'))
print(format(z/n,',.6f'))
