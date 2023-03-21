#7576
#토마토
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
    print("")

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
