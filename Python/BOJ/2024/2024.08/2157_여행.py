# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
dp = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    if a > b:
        continue
    graph[a][b] = max(graph[a][b], c) # 최댓값만 항로에 넣기

for i in range(2, n+1):
    dp[i][2] = graph[1][i] # 1에서 i까지 j개의 도시
    
for i in range(2, n+1):
    for j in range(3, m+1):
        for l in range(1, i):
            if graph[l][i] and dp[l][j-1]:
                dp[i][j] = max(dp[i][j], dp[l][j-1] + graph[l][i])
                print(dp)

print(max(dp[n]))


    
    
