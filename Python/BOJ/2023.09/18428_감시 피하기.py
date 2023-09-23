import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
teacher = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def check():
    for t in teacher: # 선생님 다 감시 시작
        x, y = t[0], t[1]
        for d in range(4): # 4방향
            nx = x + dx[d]
            ny = y + dy[d]
            # 맵 벗어나거나 장애물 만나기 전까지 감시
            while 0<= nx < n and 0<= ny < n and graph[nx][ny] !='O': 
                if graph[nx][ny] == 'S': # 학생 찾음
                    return True            
                else: # 학생 못찾으면 그방향으로 계속 감시
                    nx += dx[d]
                    ny += dy[d]
    return False
                    
def make_wall(cnt):
    if cnt==3: # 장애물 3개 세우면 감시 시작
        if(check() == False): # 학생 못 찾았을 시 감시 피하기 성공
            print("YES")
            exit(0) # 즉시 종료
        return
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                make_wall(cnt+1)
                graph[i][j] = 'X'
                
                
make_wall(0)
print("NO") # 벽 다 세워봤는데 다 감시 가능하면 NO 출력