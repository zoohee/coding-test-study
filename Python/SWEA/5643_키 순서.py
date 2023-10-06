import sys
input = sys.stdin.readline
from collections import deque

def dfs_greater(graph, start, visited):
    visited[start] = True
    count = 1
    for i in range(len(graph)):
        if not visited[i] and graph[start][i] == 1:
            count += dfs_greater(graph, i, visited)
    return count

def dfs_smaller(graph, start, visited):
    visited[start] = True
    count = 1
    for i in range(len(graph)):
        if not visited[i] and graph[i][start] == 1:
            count += dfs_smaller(graph, i, visited)
    return count

T = int(input().strip())
for t in range(1, T+1):
    n = int(input().strip())
    m = int(input().strip())
    
    # 그래프 초기화
    graph = [[0] * n for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
    
    result = 0
    
    for i in range(n):
        visited = [False] * n
        greater_count = dfs_greater(graph, i, visited) - 1  # 자기 자신은 빼기
        visited = [False] * n
        smaller_count = dfs_smaller(graph, i, visited) - 1  # 자기 자신은 빼기
        if greater_count + smaller_count == n - 1:
            result += 1
    
    print("#{} {}".format(t, result))
