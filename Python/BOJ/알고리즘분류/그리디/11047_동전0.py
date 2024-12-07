# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 4
# Url: https://www.acmicpc.net/problem/11047
# Reference: 

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0

value = [0]*N
for i in range(N):
    value[i] = int(input())

value.sort(reverse=True)
for i in range(N):
    answer += K//value[i]
    K = K%value[i]

print(answer)

