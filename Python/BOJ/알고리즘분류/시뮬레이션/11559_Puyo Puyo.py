# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline
from collections import deque

def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    temp.append((a, b))
    
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == field[x][y] and visited[nx][ny] == 0:
                queue.append((nx, ny))
                temp.append((nx, ny))
                visited[nx][ny] = 1
           
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if field[j][i] != "." and field[k][i] == ".":
                    field[k][i] = field[j][i]
                    field[j][i] = "."
                    break
    
def delete(temp):
    for a,b in temp:
        field[a][b] = "."
        
field = [list(input().rstrip()) for _ in range(12)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
while True:
    flag = 0
    visited = [[0]*6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                visited[i][j] = 1
                temp = []
                BFS(i, j)
                
                if len(temp) >= 4:
                    flag = 1
                    delete(temp)
    
    if flag == 0:
        break
    down()
    answer += 1
                
print(answer)
    