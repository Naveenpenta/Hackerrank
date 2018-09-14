#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
(a,b,c,d,e)=(0,0,0,0,0)
a=arr[1]+arr[2]+arr[3]+arr[4]
b=arr[0]+arr[2]+arr[3]+arr[4]
c=arr[0]+arr[1]+arr[2]+arr[4]
d=arr[0]+arr[1]+arr[3]+arr[4]
e=arr[0]+arr[1]+arr[2]+arr[3]
j=max(a,b,c,d,e)
k=min(a,b,c,d,e)
print(k,j)
