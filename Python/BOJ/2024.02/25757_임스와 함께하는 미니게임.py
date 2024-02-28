# 실행시간: 88ms
# 메모리: 25757KB
# 난이도: Silver 5
# Url: https://www.acmicpc.net/problem/25757
# Reference: me

import sys
input = sys.stdin.readline

n, game = input().split()
n = int(n)
players = [input().rstrip() for _ in range(n)]
players = list(set(players))

p  = 1
if game == 'Y':
    p = 1
elif game == 'F':
    p = 2
elif game == 'O':
    p = 3

print(len(players) // p)
