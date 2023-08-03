#1926
#그림
#https://ywtechit.tistory.com/70
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
    each_cnt = 1
    queue = deque() 
    queue.append((x, y)) # 첫번째 원소 튜플로 저장
    visited[x][y] = True # 첫번째 원소 방문
    
    while(queue): # queue가 비지 않는 동안
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i] # (1,0) (0,1) (-1,0) (0,-1)
            ny = y + dy[i] # 좌상우하 방문
            
            if 0 <= nx < n and 0 <= ny < m: # 그래프 크기 안이면
                if graph[nx][ny] == 1 and not visited[nx][ny]: # 그래프 원소가 1이고 방문하지 않았으면
                    visited[nx][ny] = True # 방문했다고 표시
                    queue.append((nx, ny)) # queue에 추가
                    each_cnt += 1 # 그림 크기 늘려주기
    return each_cnt
        
n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt, max_each_count = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_each_count = max(max_each_count, BFS(i, j))
 
print(cnt)
print(max_each_count)