# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/14499
# Reference: 
import sys
input = sys.stdin.readline

def turn_dice(direction):
    new_dice = [0] * 6
    hor = [0, 2, 5, 3]
    ver = [0, 4, 5, 1]
    temp = 0
    if direction == 1: # 동
        for i in range(3, -1, -1):
            if i == 3:
                new_dice[hor[0]] = dice[hor[i]]
            else:
                new_dice[hor[i+1]] = dice[hor[i]]
        new_dice[1] = dice[1]
        new_dice[4] = dice[4]
    elif direction == 2: # 서
        for i in range(4):
            if i == 0:
                new_dice[hor[3]] = dice[hor[i]]
            else:
                new_dice[hor[i-1]] = dice[hor[i]]
        new_dice[1] = dice[1]
        new_dice[4] = dice[4]
    elif direction == 3: # 북
        for i in range(4):
            if i == 0:
                new_dice[ver[3]] = dice[ver[i]]
            else:
                new_dice[ver[i-1]] = dice[ver[i]]
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
    else:
        for i in range(3, -1, -1):
            if i == 3:
                new_dice[ver[0]] = dice[ver[i]]
            else:
                new_dice[ver[i+1]] = dice[ver[i]]       
        new_dice[2] = dice[2]
        new_dice[3] = dice[3] 
        
    return new_dice

n, m, x, y, k = map(int, input().split())
mini_map = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0] * 6

for i in range(k):
    if order[i] == 1:
        if y+1 < m:
            y += 1
            dice = turn_dice(1)
        else:
            continue
    elif order[i] == 2:
        if y-1 >= 0:
            y -= 1
            dice = turn_dice(2)
        else:
            continue
    elif order[i] == 3:
        if x-1 >= 0:
            x -= 1
            dice = turn_dice(3)
        else:
            continue
    else:
        if x+1 < n:
            x += 1
            dice = turn_dice(4) # 남쪽
        else:
            continue

    if mini_map[x][y] == 0:
        mini_map[x][y] = dice[5]
    else:
        dice[5] = mini_map[x][y]
        mini_map[x][y] = 0

    print(dice[0])
        