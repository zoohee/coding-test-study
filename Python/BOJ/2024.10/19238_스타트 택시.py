# 실행시간: 296 ms
# 메모리: 34156 KB
# 난이도: Gold 2
# Url: https://www.acmicpc.net/problem/19238
# Reference: 
import sys
from collections import deque
input = sys.stdin.readline
n, m, energy = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    visited = [[-1] * n for _ in range(n)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 0
    
    while que:
        x, y = que.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
                
    return visited
    

def check(visited, people):
    i = 0
    for px, py, ax, ay in people:
        people[i].append(visited[px - 1][py - 1])
        i += 1

    people.sort(key=lambda x: (-x[4], -x[0], -x[1]))

def solve(sx, sy):
    global energy
    while people:
        visited = bfs(sx - 1, sy - 1)
        check(visited, people)
        px, py, ax, ay, dist = people.pop()

        for p in people:
            p.pop()

        visited = bfs(px - 1, py - 1)
        dist2 = visited[ax - 1][ay - 1]
        sx, sy = ax, ay

        if dist == -1 or dist2 == -1:
            print(-1)
            return

        energy -= dist
        if energy < 0:
            break

        energy -= dist2
        if energy < 0:
            break

        energy += dist2 * 2

    if energy < 0:
        print(-1)
    else:
        print(energy)  
        
solve(sx, sy)