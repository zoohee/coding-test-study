#2468
#안전 영역
from collections import deque
import sys
input = sys.stdin.readline

def water_BFS(max, i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] <= max+1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
def area_BFS(i, j):
    queue = deque()
    queue.append((0, 0))
    visited[i][j] = True
    
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_height = 0
for i in range(n):
    max_height = max(max_height, max(graph[i]))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
    
area_list = [[0] for _ in range(max_height)]
for i in range(max_height):
    visited = [[False] * n for _ in range(n)]
    
    # 물 잠기기
    for j in range(n):
        for k in range(n):
            water_BFS(i, j, k)
    
    # 구역 세기
    cnt = 0
    for j in range(n):
        for k in range(n):
            if visited[j][k] == False:
                area_BFS(j, k)
                cnt += 1
                
    area_list[i] = cnt
    
print(max(area_list))

# 높이별로 BFS 돌려서 구역개수 max값
# 물 적시는 BFS 한번
# 구역 개수 세는 BFS 한번..?