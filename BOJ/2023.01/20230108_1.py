#10807
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
v = int(input())

print(li.count(v))