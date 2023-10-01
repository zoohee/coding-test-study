import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
# abcdef 방문함, 방문안함 비트마스킹으로 체크 -> 000000~111111 -> 64개
visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]

que = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == "0":
            graph[i][j] = "."
            que.append((i, j, 0))
            break
      
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]  

while(que):
    x, y, key = que.popleft()
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        nkey = key
        
        # 현재 키를 가지고 방문한 적이 없으면
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#' and visited[nx][ny][key] == 0:
            # 대문자면 (문이면)
            if graph[nx][ny].isupper():
                # 열쇠가 없으면 continue
                if not (key & 1 << (ord(graph[nx][ny]) - ord("A"))):
                    continue
            # 소문자면 (열쇠면)
            elif graph[nx][ny].islower():
                # 키 교체
                nkey |= 1 << ord(graph[nx][ny]) - ord("a")
            # 도착지점 오면 답 출력
            elif graph[nx][ny] == "1":
                print(visited[x][y][key] + 1)
                exit()   
            que.append((nx, ny, nkey))
            visited[nx][ny][nkey] = visited[x][y][key] + 1
            
print(-1)