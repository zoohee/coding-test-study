#2577
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
 
num = list(str(a*b*c))

for i in range(len(num)):
    print(num.count(str(i)))
