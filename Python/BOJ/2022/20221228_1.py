#10093
import sys
input = sys.stdin.readline

n1, n2 = map(int,input().split())

a = min(n1, n2)
b = max(n1, n2)

num = b - a - 1
if a==b or a+1==b:
    num = 0
print(num)
for i in range(a+1, b):
    print(i, end=' ')