# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 0, -1, 0, -1, -2, -2, -1, 1, 2, 2, 1]

def bfs():
    que = deque()
    que.append((0, 0, 0))
    visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 1
    
    while que:
        x, y, cnt = que.popleft()
        if x==h-1 and y==w-1:
            return visited[x][y][cnt]-1
        
        for d in range(12):
            if d >= 4 and cnt >= k: # 말 이동 사용 횟수가 k를 초과하면 말 이동 중지
                break
            
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < h and 0 <= ny < w:
                if d >= 4: # 말 이동
                    if visited[nx][ny][cnt+1] == 0 and graph[nx][ny] == 0:
                        que.append((nx, ny, cnt+1))
                        visited[nx][ny][cnt+1] = visited[x][y][cnt] + 1
                else: # 일반 이동
                    if visited[nx][ny][cnt] == 0 and graph[nx][ny] == 0:
                        que.append((nx, ny, cnt))
                        visited[nx][ny][cnt] = visited[x][y][cnt] + 1

    return -1

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

print(bfs())


            
    
    