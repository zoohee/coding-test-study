# 실행시간: 40 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/15989
# Reference: https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-15989%EB%B2%88-123-%EB%8D%94%ED%95%98%EA%B8%B0-4-Python-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8DDP

import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]
    
for _ in range(n):
    m = int(input())
    print(dp[m])
