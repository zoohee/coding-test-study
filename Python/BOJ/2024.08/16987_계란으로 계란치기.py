# 실행시간: 3956 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/16987
# Reference: https://velog.io/@rkdalstn7221/%EB%B0%B1%EC%A4%80-16987-%EA%B3%84%EB%9E%80%EC%9C%BC%EB%A1%9C-%EA%B3%84%EB%9E%80%EC%B9%98%EA%B8%B0-Python

import sys
input = sys.stdin.readline

def plus(eggs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt += 1
    return cnt

def solution(depth, arr):
    global answer
    if depth == n:
        answer = max(answer, plus(arr))
        return
    
    if arr[depth][0] <= 0:
        solution(depth+1, arr)
    else:
        check = True
        for i in range(n):
            if depth != i and arr[i][0] > 0:
                check = False
                arr[depth][0] -= arr[i][1]
                arr[i][0] -= arr[depth][1]
                solution(depth + 1, arr)
                arr[depth][0] += arr[i][1]
                arr[i][0] += arr[depth][1]
        if check:
            solution(n, arr)
        

n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]
answer = 0
solution(0, egg)
print(answer)