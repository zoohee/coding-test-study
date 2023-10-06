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
        # 아래부터 올라와서 0 찾으면 swap
        for i in range(h-1, -1, -1):
            if graph[i][j] == 0:
                k = i
                # while(graph[k][j] != 0 and k >= 0):
                #     graph[k][j] = graph[k-1][j]
                #     k -= 1
                # if k != -1:
                #     graph[k][j] = 0
                break
        
def breaking(graph, a, b):
    visited = [[False] * w for _ in range(h)]
    que = deque()
    que.append((a, b))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while(que):
        x, y = que.popleft()
        for i in range(graph[x][y]):
            for d in range(4):
                nx = x + i*dx[d]
                ny = y + i*dy[d]
                if 0<=nx<h and 0<=ny<w and graph[nx][ny]!=0 and not visited[nx][ny]:
                    graph[nx][ny] -= 1
                    visited[nx][ny] = True
                    if(graph[nx][ny] != 0):
                        que.append((nx, ny))



def sol(origin_graph):
    # 중복순열
    ans = int(1e9)
    for perm in product(range(w), repeat=n):
        graph = copy.deepcopy(origin_graph)
        for j in [2, 2, 6]: # 열
            for i in range(h): # 행
                if graph[i][j] != 0:
                    # 벽돌 부시기
                    breaking(graph, i, j)
                    # 벽돌 떨어지기
                    # drop_brick(graph)
                    break
        print_graph(graph)
        ans = min(ans, count_brick(graph))
        break
    return ans

T = int(input())
for t in range(T):
    n, w, h = map(int, input().split())
    origin_graph = [list(map(int, input().split())) for _ in range(h)]
    print(sol(origin_graph))

    

# 1
# 3 10 10
# 0 0 0 0 0 0 0 0 0 0
# 1 0 1 0 1 0 0 0 0 0
# 1 0 3 0 1 1 0 0 0 1
# 1 1 1 0 1 2 0 0 0 9
# 1 1 4 0 1 1 0 0 1 1
# 1 1 4 1 1 1 2 1 1 1
# 1 1 5 1 1 1 1 2 1 1
# 1 1 6 1 1 1 1 1 2 1
# 1 1 1 1 1 1 1 1 1 5
# 1 1 7 1 1 1 1 1 1 1