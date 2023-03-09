#10773
import sys
input = sys.stdin.readline

k = int(input())
stack = []

for i in range(k):
    integer = int(input())
    if integer == 0:
        stack.pop()
    else:
        stack.append(integer)
        
print(sum(stack))