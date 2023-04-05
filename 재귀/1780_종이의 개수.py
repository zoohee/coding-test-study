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
                return
    if paper[x][y] == -1:
        cnt[0] += 1
        print(-1)
    elif paper[x][y] == 0:
        cnt[1] += 1
        print(0)
    elif paper[x][y] == 1:
        cnt[2] += 1
        print(1)
    
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

REC(0, 0, n)
for i in range(3):
    print(cnt[i])