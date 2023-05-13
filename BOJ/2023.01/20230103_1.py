#1475
import sys
import math
input = sys.stdin.readline

num = list(input())
li = [""] * 10

for i in range(10):
    li[i] = num.count(str(i))
    
# round함수는 2.5를 2로 반올림함..
tmp = int(math.ceil((li[6] + li[9]) / 2))
li[6] = tmp
del li[9:]

print(max(li))