# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/2623
# Reference: 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0]):
        graph[arr[j]].append(arr[j+1])
        indegree[arr[j+1]] += 1