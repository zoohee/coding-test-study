#2752
import sys
input = sys.stdin.readline

num = list(map(int,input().split()))
num.sort()
print(num[0], num[1], num[2])
