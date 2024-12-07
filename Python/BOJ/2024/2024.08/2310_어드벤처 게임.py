# 실행시간: 620 ms
# 메모리: 117420 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/2310
# Reference: Pypy3
from collections import deque
import sys
input = sys.stdin.readline

def solution(maze_list):
    visited = [-1]*n  
    check = False

    if maze_list[0][0] == 'T':
        return 'No'
    elif maze_list[0][0] == 'L':
        q = deque([(0, maze_list[0][1])])
        visited[0] = maze_list[0][1]
    else :
        q = deque([(0, 0)])
        visited[0] = 0

    while q:
        cur, money = q.popleft()
        if cur == n-1 :
            check = True
            break
        
        for node in maze_list[cur][2] :
            if maze_list[node][0] == 'T' :
                if maze_list[node][1] > money :
                    continue
                next_money = money - maze_list[node][1]
            elif maze_list[node][0] == 'L' :
                next_money = max(money, maze_list[node][1])
            else :
                next_money = money
            if visited[node] < next_money :
                visited[node] = next_money
                q.append((node, next_money))

    return 'Yes' if check else 'No'

while True :
    n = int(input())
    if not n :
        break
    maze_list = list()
    for _ in range(n) :
        typ, money, *next_list = input().split()
        next_list = list(map(lambda x: int(x)-1, next_list[:-1]))
        maze_list.append([typ, int(money), next_list])

    print(solution(maze_list))