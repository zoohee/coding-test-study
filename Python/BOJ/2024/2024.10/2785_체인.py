# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
chain = list(map(int, input().split()))
chain.sort()

cnt = 0
use = 0

for c in chain:
    if c == n-1:
        print(use + c)
        exit(0)
    elif c > n-1:
        print(use + n -1)
        exit(0)
    else:
        n -= c + 1
        use += c

print(cnt)
        
