import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
    
def dijkstra(start):
    q = []
    distance = [INF] * (N+1)
    
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    
    while(q):
        cur, dist = heapq.heappop(q)
        if distance[cur] < dist: # 최단거리 아니면 건너뛰기
            continue  
        
        for next, weight in graph[cur]:
            cost = dist + weight # 다음 노드까지 거리 계산
            if distance[next] > cost: # 계산된 값이 더 적으면 교체
                distance[next] = cost
                heapq.heappush(q, (next, cost))
                
    return distance

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))
    
answer = 0
back = dijkstra(X)
for i in range(1, N+1):
    go = dijkstra(i)
    answer = max(answer, go[X] + back[i])

print(answer)