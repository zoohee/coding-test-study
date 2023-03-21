#7562
#나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline

def BFS(l, dest_x, dest_y):
    while(queue):
        x, y = queue.popleft()
        
        if x == dest_x and y == dest_y:
            return
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx == dest_x and ny == dest_y:
                visited[nx][ny] = visited[x][y] + 1
                return
            
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                
                
                
n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(n):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    queue = deque()
    
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    
    # 8 / 0 0 / 7 0
    # 8x8 사이즈 / 0,0에서 시작 / 7,0에 도착
    # 그래프 만들기
    
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    
    BFS(l, dest_x, dest_y)
    
    answer = 0
    for i in range(l):
        answer = max(answer, max(visited[i]))
    print(answer-1)
    