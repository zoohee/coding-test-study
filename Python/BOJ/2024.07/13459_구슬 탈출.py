# 실행시간: 64 ms
# 메모리:34136  KB
# 난이도: Gold 1
# Url: https://www.acmicpc.net/problem/13459
# Reference: 
import sys
input = sys.stdin.readline
from collections import deque

def move(i, j, dx, dy):
    c = 0
    while s[i + dx][j + dy] != "#" and s[i][j] != "O": # 장애물 안 만나면 그 방향으로 쭉 가기
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs():
    while q:
        ri, rj, bi, bj, d = q.popleft()
        
        if d > 10: # 10번 이하로 움직이기
            break
        
        for i in range(4):
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            
            if s[nbi][nbj] != "O":
                if s[nri][nrj] == "O": # 구멍 만나면 탈출 성공
                    print(1)
                    return
                if nri == nbi and nrj == nbj: # 빨간 구슬과 파란 구슬이 같은 위치 일 때,
                    if rc > bc: # 더 많이 이동한(먼저 이동 시작한) 구슬을 한 칸 뒤로
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visited[nri][nrj][nbi][nbj]: # 방문 처리
                    visited[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, d + 1])
                    
    print(0)
        
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
s = []

for i in range(n):
    a = list(input())
    s.append(a)
    for j in range(m): # 시작점 찾기
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j
            
q = deque()
q.append([ri, rj, bi, bj, 1])
visited[ri][rj][bi][bj] = True
bfs()