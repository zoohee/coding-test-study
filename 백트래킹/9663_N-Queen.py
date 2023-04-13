# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

def n_queens(col, i):
    global answer
    n = len(col) - 1
    if (promising(i, col)):
        if i == n:
            answer += 1
            print(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(col, i+1)
                
def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        # 좌우 or 대각선
        # board[n] == board[i] -> 같은 열에 놓이게 되므로, 유망하지 않다.
        # n-i == abs(board[n] - board[i] -> 행에서의 차이와 열에서의 차이의 절댓값이 같은 것이 대각선.
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

n = int(input())
col = [0] * (n+1)
answer = 0
n_queens(col, 0)
print(answer)
  
  # 기본 가정: 같은 행에는 퀸을 놓지 않는다.
  # 유망 함수의 구현: 같은 열이나 같은 대각선에 놓이는 지 확인
  # n=4 일 때,
  # [2, 4, 1, 3] -> 1행2열, 2행4열, 3행1열, 4행3열
  # [3, 1, 4, 2] -> 1행3열, 2행1열, 3행4열, 4행2열