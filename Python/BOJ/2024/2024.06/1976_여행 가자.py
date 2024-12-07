# 실행시간: 68 ms
# 메모리: 34044 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/1976
# Reference: https://daekyojeong.github.io/posts/BOJ92/

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = True
    
    while que:
        node = que.popleft()
        for idx, item in enumerate(graph[node]):
            if item and visited[idx] == 0:
                visited[idx] = True
                que.append(idx)
    

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
visited = [False] * n

bfs(plan[0]-1)

for p in plan:
    if visited[p-1] == 0:
        print('NO')
        exit(0)
print('YES')        

