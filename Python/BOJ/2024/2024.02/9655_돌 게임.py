# 실행시간: 44ms
# 메모리: 31120KB
# 난이도: Silver 5
# Url: https://www.acmicpc.net/problem/9655
# Reference: me
import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print("SK")
    exit(0)
if n == 2:
    print("CY")
    exit(0)

a = n % 3
if a == 0 or a == 2:
    if (n // 3) % 2 == 0:
        print("CY")
    else:
        print("SK") 
else:
    if (n // 3) % 2 == 0:
        print("SK")
    else:
        print("CY") 