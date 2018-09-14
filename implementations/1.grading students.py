import sys

def solve(grades):
    # Complete this function
    for i in range(0,n):
        if(grades[i]>37):
            t=grades[i]%5
            if(t==3):
                grades[i]+=2
            if(t==4):
                grades[i]+=1
    return grades
        
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
