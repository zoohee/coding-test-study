# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hbg = input()

for i in range(len(hbg)):
    if hbg[i]=='H':
        print("햄버거")
    else:
        print("사람")
        
    