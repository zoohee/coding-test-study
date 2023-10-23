import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
city = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    city[a].append((b, c))

start, end = map(int, input().split())

nearnest = [start] * (n + 1)
distance = [1e9] * (n + 1) # 무한 값으로 초기화

q = [(0, start)]
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]: # 최단 거리 아니면 넘어가기
        continue
    
    for next, nextDist in city[now]: # 거쳐가는 거리 검사
        cost = nextDist + dist
        if cost < distance[next]:
            distance[next], nearnest[next] = cost, now
            heapq.heappush(q, (cost, next))

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = nearnest[tmp]

ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(" ".join(ans))