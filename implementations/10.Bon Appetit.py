import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    l=ar[k]
    ar.remove(l)
    s=sum(ar)
    ll=s//2
    if(b>ll):
        return(b-ll)
    else:
        return("Bon Appetit")

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
