import sys
input = sys.stdin.readline
from itertools import product
import copy
from collections import deque

def print_graph(graph):
    print("==================")
    for i in range(h):
        for j in range(w):
            print(graph[i][j], end=" ")
        print()

def count_brick(graph):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] != 0:
                cnt += 1
    return cnt

def drop_brick(graph):
    for j in range(w):
        que = deque()  # 비어 있는 공간을 채울 벽돌들을 담을 스택
        for i in range(h-1, -1, -1):
            if graph[i][j] != 0:
                que.append(graph[i][j])
                graph[i][j] = 0  # 현재 위치를 비움
        # 스택에 담긴 벽돌들을 아래에서부터 채워넣음
        idx = h - 1
        while que:
            graph[idx][j] = que.popleft()
            idx -= 1
        
def breaking(graph, x, y):
    # 벽돌이 부서질 위치
    size = graph[x][y]
    graph[x][y] = 0

    # 주변 벽돌을 확인하며 부수기
    for d in range(4):
        for i in range(1, size):
            nx, ny = x + dx[d] * i, y + dy[d] * i
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 0:
                breaking(graph, nx, ny)

def sol(origin_graph):
    # 중복순열
    ans = int(1e9)
    for perm in product(range(w), repeat=n):
        graph = copy.deepcopy(origin_graph)
        for j in perm: # 열
            for i in range(h): # 행
                if graph[i][j] != 0:
                    # 벽돌 부시기
                    breaking(graph, i, j)
                    # 벽돌 떨어지기
                    drop_brick(graph)
                    break
            # print_graph(graph)
        ans = min(ans, count_brick(graph))

    return ans

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    n, w, h = map(int, input().split())
    origin_graph = [list(map(int, input().split())) for _ in range(h)]
    print("#",t," ",sol(origin_graph), sep="")