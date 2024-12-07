# 실행시간: 112ms
# 메모리: 46236KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/13305
# Reference: me
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost = 0
min_price = oil[0]
for i in range(n-1):
    if oil[i] < min_price:
        min_price = oil[i]
    cost += min_price*dist[i]

print(cost)