# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(a, b, arr, visited, room_num):
    q = deque()
    q.append((a, b))
    visited[a][b] = room_num
    room_size = 1
    while q:
        x, y = q.popleft()
        info = bin(arr[x][y])[2:]
        info = '0'*(4-len(info))+info
        for k, bit in enumerate(info):

            if bit == '0':
                nx = x + dx[k]
                ny = y + dy[k]
                if not visited[nx][ny]:
                    visited[nx][ny] = room_num
                    q.append((nx, ny))
                    room_size += 1

            if bit == '1':
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    if visited[nx][ny] != room_num:
                        room_dict[visited[nx][ny]].add(room_num)
                        room_dict[room_num].add(visited[nx][ny])
    return room_size


visited = [[0 for _ in range(m)] for _ in range(n)]
room_count = 0  # 방의 개수
room_dict = defaultdict(set)
room_info = defaultdict(int)
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            room_count += 1
            size = bfs(i, j, arr, visited, room_count)
            room_info[room_count] = size

break_max = 0
for a in room_dict:
    for b in room_dict[a]:
        break_max = max(break_max, room_info[a]+room_info[b])

print(room_count, max(room_info.values()), break_max)