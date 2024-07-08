import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
    
