import sys
input = sys.stdin.readline

cnt = [0, 0]
def REC(n, x, y):
    global cnt
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                REC(n//2, x, y) # 1사분면
                REC(n//2, x, y+n//2) # 2사분면
                REC(n//2, x+n//2, y) # 3사분면
                REC(n//2, x+n//2, y+n//2) # 4사분면
                return
                        
    if paper[x][y] == 0:
        cnt[0] += 1
        # print(0)
    elif paper[x][y] == 1:
        cnt[1] += 1
        
                    
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
REC(N, 0, 0)
for i in range(2):
    print(cnt[i])

