# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
from collections import deque
import sys
input = sys.stdin.readline

# 가장 약한 포탑 공격자 선정
def select_attacker(time):
    min_tower = 1e9
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                min_tower = min(min_tower, graph[i][j])
                        
    attacker = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == min_tower:
                attacker.append((i, j, attack_time[i][j]))
    
    attacker.sort(key = lambda x: (-x[2], -(x[0]+x[1]), -x[1]))
    select_x, select_y = attacker[0][0], attacker[0][1]
    graph[select_x][select_y] += (n+m)
    attack_time[select_x][select_y] = time
    
    return select_x, select_y

def attack(x, y):
    max_tower = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and (i, j) != (x, y):
                max_tower = max(max_tower, graph[i][j])
    
    victim = []
    for i in range(n):
        for j in range(m):
            if max_tower == graph[i][j]:
                victim.append((i, j, attack_time[i][j]))
    
    victim.sort(key = lambda x: (x[2], x[0]+x[1], x[1]))
    select_x, select_y = victim[0][0], victim[0][1]
    
    return select_x, select_y

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def laser_attack(a_x, a_y, v_x, v_y):
    que = deque()
    que.append((a_x, a_y))
    visited = [[False]*m for _ in range(n)]
    visited[a_x][a_y] = True
    back_trace = [[None]*m for _ in range(n)]
    
    while que:
        x, y = que.popleft()
        if x == v_x and y == v_y:
            return back_trace
        
        for d in range(4):
            nx = (x + dx[d]) % n
            ny = (y + dy[d]) % m
                
            if graph[nx][ny] > 0 and not visited[nx][ny]:
                back_trace[nx][ny] = (x, y)
                visited[nx][ny] = True
                que.append((nx, ny))
    
    return back_trace

dxx = [-1, -1, -1, 0, 0, 1, 1, 1]
dyy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bomb_attack(a_x, a_y, v_x, v_y):
    graph[v_x][v_y] -= graph[a_x][a_y]
    route = [(v_x, v_y), (a_x, a_y)]
    for d in range(8):
        nx = (v_x + dxx[d]) % n
        ny = (v_y + dyy[d]) % m
        
        if (nx, ny) == (a_x, a_y):
            continue
        
        graph[nx][ny] -= graph[a_x][a_y] // 2
        route.append((nx, ny))
        
    return route
            
def minus_abillity(back_trace, a_x, a_y, v_x, v_y):
    c_x, c_y = v_x, v_y
    graph[c_x][c_y] -= graph[a_x][a_y]
    route = [(v_x, v_y)]
    
    while True:
        c_x, c_y = back_trace[c_x][c_y]
        route.append((c_x, c_y))
        if c_x == a_x and c_y == a_y:
            return route
        graph[c_x][c_y] -= graph[a_x][a_y] // 2
        
def destroy():
    for i in range(n):
        for j in range(m):
            graph[i][j] = max(graph[i][j], 0)
            
def repair(route):
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and (i, j) not in route:
                graph[i][j] += 1
    
def is_end():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                cnt += 1
    if cnt == 1:
        return True
    else:
        return False
                
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

attack_time = [[0] * m for _ in range(n)]
for t in range(1, k+1):
    if is_end():
        break
    a_x, a_y = select_attacker(t)
    v_x, v_y = attack(a_x, a_y)
    back_trace = laser_attack(a_x, a_y, v_x, v_y)
        
    if back_trace[v_x][v_y] != None:
        # 공격력 낮추기
        route = minus_abillity(back_trace, a_x, a_y, v_x, v_y)
        
    else:
        # 포탄공격
        route = bomb_attack(a_x, a_y, v_x, v_y)
    
    destroy()
    repair(route)
        
answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, graph[i][j])
print(answer)