# 실행시간: 136ms
# 메모리: 31120KB
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/3758
# Reference: 
import sys
input = sys.stdin.readline

case = int(input().rstrip())

for i in range(case):
    n, k, t, m = map(int, input().split())
    score = [[0]*k for _ in range(n)]
    submit = [0]*n
    time = [0]*n
    
    for h in range(m):
        i, j, s = map(int,input().split())
        score[i-1][j-1] = max(score[i-1][j-1], s)
        submit[i-1] += 1
        time[i-1] = h
    
    line = []
    for h in range(n):
        line.append([sum(score[h]), submit[h], time[h], h])
    
    line.sort(key = lambda x : (-x[0], x[1], x[2]))
    
    for rank in range(n):
        if line[rank][3] == t - 1:
            print(rank+1)
     