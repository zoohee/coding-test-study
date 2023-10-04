import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, start, end):
    n = len(graph)
    visited = [False] * n

    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in range(n):
            if not visited[neighbor] and graph[node][neighbor] == 1:
                if neighbor == end:
                    return True
                queue.append(neighbor)
                visited[neighbor] = True
    
    return False

T = int(input())
for t in range(T):
    n = int(input())
    m = int(input())
    graph = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    print(graph)
    ans = 0
    # 모든 정점이 한 정점과 인접하거나 지나갈 수 있으면 카운트하기
    for i in range(1, n+1):
        cnt = 0
        for j in range(i, n+1):
            if bfs(graph, j, i):
                cnt += 1
        if cnt == n:
            ans += 1
    
    print(ans)

