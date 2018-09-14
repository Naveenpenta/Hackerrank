#!/bin/python3
import sys

def solve(year):
    # Complete this function
    if(year%400==0):
        return('12.09.%d' %(year))
        break;
    elif(year%4==0 and year%100!=0):
        return('12.09.%d' %(year))
    else:
        return('13.09.%d' %(year))
year = int(input().strip())
result = solve(year)
print(result)
