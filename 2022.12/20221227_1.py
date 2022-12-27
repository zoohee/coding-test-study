#2576
import sys
input = sys.stdin.readline

num = []

for i in range(7) :
    a = int(input())
    if a%2 != 0 :
        num.append(a)    
        
if len(num) == 0 :
    print(-1)
else :
    print(sum(num))
    print(min(num))

