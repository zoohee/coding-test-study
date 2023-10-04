import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = []
for _ in range(n):
    x, y = map(int, input().split())
    ladder.append((x, y))

snake = []
for _ in range(n):
    x, y = map(int, input().split())
    snake.append((x, y))