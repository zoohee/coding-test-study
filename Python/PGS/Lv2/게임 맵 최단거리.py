# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3
# Reference: me

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    que = deque()
    que.append((0, 0, 0))
    
    while que:
        x, y, dist = que.popleft()
        
        if x == n-1 and y == m-1:
            return dist+1
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                que.append((nx, ny, dist+1))
                
    return -1