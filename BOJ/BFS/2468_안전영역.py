from collections import deque
import sys
input = sys.stdin.readline

def BFS(a, b, max):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                # 최대 높이보다 높을 때 방문처리
                if graph[nx][ny] > max and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

#최고 높이 구하기
max_height = 0
for i in range(n):
    max_height = max(max_height, max(graph[i]))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
for i in range(max_height):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    
    for j in range(n):
        for k in range(n):
            # 최대 높이보다 높은 영역 구하기 (안전영역)
            if graph[j][k] > i and visited[j][k] == 0:
                BFS(j, k, i)
                cnt += 1
    
    answer = max(answer, cnt)
    
print(answer)