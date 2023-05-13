# 시간복잡도: 
# 최악시간: 
# 난이도: Gold 3
# Url: https://www.acmicpc.net/problem/18808
# Reference: 
import sys
input = sys.stdin.readline

# 시계방향으로 90도 회전한 배열을 반환한다.
def rotate(arr):
    n = len(arr)
    m = len(arr[0])
    
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

# 스티커를 붙일 수 있다면 True, 아니라면 False를 반환한다.
def check(tmp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            if tmp[i+sy][j+sx] + sticker[sy][sx] > 1:
                return False
    return True

# laptop에 스티커를 붙인다.
def attach(tmp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            tmp[i+sy][j+sx] += sticker[sy][sx]
    return
    
if __name__ == '__main__':
    N, M, k = map(int, input().split())
    laptop = [[0] * M for _ in range(N)]
    
    for _ in range(k):
        r, c = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(r)]
    
        chk = False
        cnt = 0
        while cnt < 4:
            if chk == True:
                break
            for i in range(N - len(sticker) + 1):
                if chk == True:
                    break
                for j in range(M - len(sticker[0]) + 1):
                    if check(laptop, sticker):
                        attach(laptop, sticker)
                        chk = True
                        break
            sticker = rotate(sticker)
            cnt += 1

    answer = 0
    for i in range(N):
        for j in range(M):
            answer += laptop[i][j]

    print(answer)
             
