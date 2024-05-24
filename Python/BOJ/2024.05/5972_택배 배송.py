# 실행시간: 224ms
# 메모리: 51424KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/5972
# Reference: 
import sys
import heapq
input = sys.stdin.readline
INF = 1e8

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    
    while que:
        dist, now = heapq.heappop(que) # 가장 작은 거리
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:     # 연결된 모든 노드 탐색
            if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
                distance[i[0]] = dist+i[1]
                heapq.heappush(que, (dist+i[1], i[0]))
    
    return distance[n]
                
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 1~n까지의 최단경로
print(dijkstra(1))
        