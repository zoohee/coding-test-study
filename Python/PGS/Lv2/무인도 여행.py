from collections import deque

def solution(maps):
    answer = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    def bfs(i, j):
            cnt = 0
            que = deque()
            que.append((i, j))
            visited[i][j] = True

            while(que):
                x, y = que.popleft()
                # 연결된 땅의 값을 전부 합침
                cnt += int(maps[x][y])

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 연결되어 있으면 계속 큐에 추가
                    if 0 <= nx < len(maps) and 0<= ny < len(maps[0]):
                        if visited[nx][ny] == False and maps[nx][ny] != 'X':
                            visited[nx][ny] = True
                            que.append((nx, ny))
            return cnt
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            # 땅 발견하면 bfs 시작
            if visited[i][j] == False and maps[i][j] != 'X':
                answer.append(bfs(i, j))
                
    if len(answer)==0:
        return [-1]
    else:
        answer.sort()
        return answer