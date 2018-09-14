#!/bin/python3

import sys

def getTotalX(a, b):
    # Complete this function
    l=[]
    a_list=[i for i in range(1,b[0]+1)]
    l=[i for i in a_list if all(i%j==0 for j in a)]
   # print(l)
    #print([i for i in l if all(i%j==0 for j in b) ])
    c1=0
    for i in range(0,len(l)):
        c=0
        for j in range(0,m):
            if(b[j]%l[i]==0):
                   c=c+1
            if(c==m):
                   c1=c1+1
    return(c1)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
