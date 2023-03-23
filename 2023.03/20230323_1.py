#16948
#데스 나이트
from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    queue = deque()
    queue.append((r1, c1))
    
    while(queue):
        r, c = queue.popleft()
        
        if r == r2 and c == c2:
            return visited[r2][c2]
        
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
    
    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * n for _ in range(n)]

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

print(BFS())