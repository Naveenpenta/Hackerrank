import sys
import collections

def sockMerchant(n, ar):
    # Complete this function
    a=collections.Counter(ar)
    s=0
    for i in a.values():
        s+=i//2
    return(s)
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
