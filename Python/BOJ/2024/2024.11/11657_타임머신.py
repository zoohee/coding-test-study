# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = [[1e9] * (n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     graph[i][i] = 0

# for _ in range(m):
#     s, e, w = map(int, input().split())
#     graph[s][e] = min(graph[s][e], w)
    
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == 1e9:
#             print(0, end = " ")
#         else:
#             print(graph[i][j], end = " ")
#     print()

import sys
input = sys.stdin.readline
MAX = sys.maxsize

N, M = map(int, input().split())
bus = []
for _ in range(M):
    a, b, time = map(int, input().split())
    bus.append((a, b, time))
dist = [MAX] * (N+1)


def bf(start):
    dist[start] = 0
    for k in range(N):
        for i in range(M):
            city, ncity, time = bus[i]
            if dist[city] != MAX and dist[ncity] > dist[city] + time:
                dist[ncity] = dist[city] + time
                if k == N-1:
                    return True
    return False

if bf(1):
  print('-1')
else:
  for i in range(2, N+1):
    if dist[i] == MAX:
      print('-1')
    else:
      print(dist[i])