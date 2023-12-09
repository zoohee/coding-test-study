import sys
input = sys.stdin.readline
from collections import deque
    
def bfs():
    que = deque()
    que.append((house_x, house_y))
    while que:
        x, y = que.popleft()
        if abs(x - fes_x) + abs(y - fes_y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    que.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return

T = int(input())
for t in range(T):
    n = int(input())
    store = []
    beer = 20
    house_x, house_y = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        store.append((x, y))
    fes_x, fes_y = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    bfs()