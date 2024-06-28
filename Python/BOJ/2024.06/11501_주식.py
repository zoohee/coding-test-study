# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    benefit = 0

    max_price = 0 
    for i in range(len(stock)-1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else: 
            benefit += max_price - stock[i]

    print(benefit)