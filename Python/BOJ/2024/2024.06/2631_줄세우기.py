# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 

import sys
input = sys.stdin.readline

n = int(input().rstrip())
kids = [int(input().rstrip()) for _ in range(n)]
kids = [0] + kids

# 가장 긴 증가하는 부분 수열 찾기
dp = [1]*(n+1)
for i in range(1, n+1):
    for j in range(1, i):
        if kids[j] < kids[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))