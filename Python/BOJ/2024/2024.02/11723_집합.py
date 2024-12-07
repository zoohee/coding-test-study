# 실행시간: 3684ms
# 메모리: 31120KB
# 난이도: Silver 5
# Url: https://www.acmicpc.net/problem/11723
# Reference: me
import sys
input = sys.stdin.readline
m = int(input())

s = []
for i in range(m):
    str = input().rstrip()
    
    if str == "all":
        s = [i for i in range(1, 21)]
        continue
    elif str == "empty":
        s = []
        continue
    
    c, n = str.split()
    num = int(n)
    
    if c == "add":
        if num not in s:
            s.append(num)
    elif c == "remove":
        if num in s:
            s.remove(num)
    elif c == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif c == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.append(num)