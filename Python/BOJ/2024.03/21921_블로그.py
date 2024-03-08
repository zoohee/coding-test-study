# 실행시간: 164ms
# 메모리: 58784KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/21921
# Reference: me
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
today = list(map(int, input().split()))

ans = 0
for i in range(x):
    ans += today[i]

max_today = ans
duration = 1
for i in range(x, len(today)):
    ans += today[i]
    ans -= today[i-x]
    if max_today == ans:
        duration += 1
    if max_today < ans:
        max_today = ans
        duration = 1
    
if max_today == 0:
    print("SAD")
else:
    print(max_today)
    print(duration)