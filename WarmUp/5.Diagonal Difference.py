#!/bin/python3

import sys
def func(n):
    s=0
    d=0
    for i in range(n):
        s+=(a[i][i])
    for j in range(n):
        d+=a[j][n-(j+1)]
    return(abs(s-d))

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
k=func(n)
print(k)
