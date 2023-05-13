import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
vis = [[0] * col for _ in range(row)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
arr = []
for _ in range(row):
    arr.append(list(map(int, sys.stdin.readline().split())))

def bfs(i, j):
    if vis[i][j] == 1:
        return 0
    area = 1
    vis[i][j] = 1 # 방문 표시
    queue.append([i, j])
    while queue:
        i, j = queue.popleft()
        for dir in range(4):
            nx = i + dx[dir]
            ny = i + dy[dir]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if arr[nx][ny] != 1 or vis[nx][ny]:
                continue
            vis[nx][ny] = 1
            queue.append([nx, ny])
            area += 1
    return area
    
areas = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]:
            areas.append(bfs(i, j))

print(areas)
cnt = len([i for i in areas if i])
print(cnt)
print(max(areas))