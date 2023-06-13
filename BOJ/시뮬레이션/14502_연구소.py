# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/3190
# Reference: https://great-park.tistory.com/104
# PyPy3만 통과
import sys
input = sys.stdin.readline
from collections import deque
import copy

def count_element(matrix, target):
    return sum(row.count(target) for row in matrix)

def BFS():
    queue = deque()
    new_graph = copy.deepcopy(graph)
    
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 2:
                queue.append((i, j))
    
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = 2 # 바이러스 퍼짐
                    queue.append((nx, ny))
                    
    global result
    cnt = 0
    cnt = count_element(new_graph, 0)
    result = max(result, cnt)

def make_wall(count):
    if count == 3:
        BFS()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0
                
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0
make_wall(0)
print(result)