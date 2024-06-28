# 실행시간: 44 ms
# 메모리: 31120 KB
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/20006
# Reference: me
import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    level, player = input().split()
    level = int(level)
    check = False
    
    for room in rooms:
        if room and room[0][0] - 10 <= level and room[0][0] + 10 >= level and len(room) < m:
            room.append((level, player))
            check = True
            break
    
    if not check:
        rooms.append([(level, player)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key=lambda x: x[1])
    for r in room:
        print(r[0], r[1])
