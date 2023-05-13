import sys
input = sys.stdin.readline

answer = []
def REC(n, x, y):
    tmp = quad[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != quad[i][j]:
                answer.append("(")
                REC(n//2, x, y) # 1사분면
                REC(n//2, x, y+n//2) # 2사분면
                REC(n//2, x+n//2, y) # 3사분면
                REC(n//2, x+n//2, y+n//2) # 4사분면
                answer.append(")")
                return
    answer.append(tmp)
    
N = int(input())
# 개행 엔터 없이 입력
quad = [list(map(int, input().rstrip())) for _ in range(N)] 
REC(N, 0, 0)
print("".join(map(str,(answer))))