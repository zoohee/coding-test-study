# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
    
def dijkstra(start):
    visited = [INF] * (n+1)
    visited[start] = 0
    cnt = 0
    end = 0
    queue = [[0, start]]
    
    while queue:
        w, cur = heapq.heappop(queue)
        if visited[cur] < w:
            continue
        for dest, wei in graph[cur]:
            cost = visited[cur] + wei
            if visited[dest] > cost:
                visited[dest] = cost
                heapq.heappush(queue, [cost, dest])
    for t in visited:
        if t < INF:
            cnt += 1
            if t > end:
                end = t
                
    return cnt, end

test_case = int(input())
for _ in range(0, test_case):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append([a, s])
    
    cnt, end = dijkstra(c)
    print(cnt, end)