a = [1,4,4,4,4,4,5,4,3]
import collections
'''n=int(input())
a=list(map(int,input().strip().split(' ')))
print(a)'''
'''from itertools import groupby
l=[len(list(group)) for key, group in groupby(a)]
print(max(l))'''
#my_dict = {i:a.count(i) for i in a}
my_dict=collections.Counter(a)
#print(my_dict)
#print(max(my_dict))
#print((max(my_dict.values())))
k=max(my_dict.values())
#print(my_dict.items())
#print(k)
for name,i in my_dict.items():
    #print(name,i)
    if(i==k):
        print(name)
