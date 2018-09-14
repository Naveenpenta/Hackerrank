#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    sum1=x1+v1
    sum2=x2+v2
    count=0
    while(count<=10000):
        if(sum1==sum2):
            break;
        else:
            sum1=sum1+v1
            sum2=sum2+v2
        count=count+1
    if(sum1==sum2):
        return("YES")
    else:
        return("NO")
   

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
