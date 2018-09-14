#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
count=0
k=0
for i in range(0,m):
    k=a+(apple[i])
    if(k<=t and k>=s):
        count=count+1
print(count)
count1=0
k1=0
for i in range(0,n):
    k1=b+(orange[i])
    if(k1<=t and k1>=s):
        count1=count1+1
print(count1)
