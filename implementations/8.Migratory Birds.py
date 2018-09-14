#!/bin/python3

import sys
import collections

def migratoryBirds(n, ar):
    # Complete this function
    my_dict=collections.Counter(ar)
#print(my_dict)
#print(max(my_dict))
#print((max(my_dict.values())))
    k=max(my_dict.values())
#print(my_dict.items())
#print(k)
    for name,i in my_dict.items():
    #print(name,i)
        if(i==k):
            return(name)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
