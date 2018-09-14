import sys
def solve(n,s,d,m):
    c=0
    for i in range(0,len(s)):
        j=i+2
        ss=sum(s[i:j])
        if(ss==d):
            c=c+1
    return(c)
n=int(input())
s=list(map(int,input().strip().split(' ')))
d,m=input().strip().split(' ')
d,m=[int(d),int(m)]
result=solve(n,s,d,m)
print(result)
