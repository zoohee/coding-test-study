import sys
input = sys.stdin.readline

cnt = [0, 0, 0]
def REC(x, y, length):
    global cnt
    for i in range(x, x+length):
        for j in range(y, y+length):
            if paper[x][y] != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        REC(x+length//3*k, y+length//3*l, length//3)
                        # 재귀를 9번 돌림
                        # (0,0,3) / (0,3,3) / (0,6,3)
                        # (3,0,3) / (3,3,3) / (3,6,3)
                        # (6,0,3) / (6,3,3) / (6,6,3)
                return
    
    # 한 박스 안에서 다른 게 없으면 조건문에 걸려서 재귀 안 돌고
    # 카운트를 추가해준다. (종이 완성)
    if paper[x][y] == -1:
        cnt[0] += 1
        # print(-1)
    elif paper[x][y] == 0:
        cnt[1] += 1
        # print(0)
    elif paper[x][y] == 1:
        cnt[2] += 1
        # print(1)
    
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

REC(0, 0, n)
for i in range(3):
    print(cnt[i])