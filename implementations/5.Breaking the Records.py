#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    low=s[0]
    high=s[0]
    (h,l)=(0,0)
    for i in range(1,n):
       # print(s[1])
       # print(s[n-1])
        if(high < s[i]):
            h=h+1
            high=s[i]
        if(low > s[i]):
            l=l+1
            low=s[i]
    return(h,l)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
