import sys
h = list(map(int,input().strip().split(' ')))
print(h)
letters = 'abcdefghijklmnopqrstuvwxyz'
letter_dict = dict( zip( list( letters ), h ))
print(list(letters))
print(letter_dict)
word = input().strip()
print([letter_dict[x] for x in letter_dict if x in word])
print(len(word) * max([ letter_dict[x] for x in letter_dict if x in word ]))
    
