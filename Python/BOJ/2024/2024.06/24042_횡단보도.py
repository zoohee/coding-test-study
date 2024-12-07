# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append((i, b))
    arr[b].append((i, a))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    visited = [sys.maxsize for _ in range(N+1)]
    visited[1] = 0
    while q:
        time, node = heapq.heappop(q)
        if node == N:
            return time
        if visited[node] < time:
            continue
        for i, nnode in arr[node]:
            # node에 존재하는 횡단보도들의 i를 이용해서 ntime을 설정
            # 횡단보도에 불이 켜지는 시간은 항상 현재 시간 이상
            ntime = i+((time-i)//M)*M if (time-i)%M==0 else i+((time-i)//M+1)*M
            if visited[nnode] > ntime+1:
                visited[nnode] = ntime+1
                heapq.heappush(q, (ntime+1, nnode))


print(dijkstra())