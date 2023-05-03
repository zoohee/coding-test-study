# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 비어있는 칸 중심
# [현재 학생의 좋아하는 학생이 인접칸에 몇명인지, 빈칸이 몇갠지, 행, 열]
def simulation():
    global input_info
    for i in range(n**2):
        like_empty_num = []
        input_info = students[i]
        for j in range(1, n+1):
            for k in range(1, n+1):
                like = 0
                empty = 0
        # 1-1. 현재 학생의 좋아하는 학생이 인접 칸에 몇 명인지
                for l in range(4):
                    nx = j + dx[l] 
                    ny = k + dy[l]
                    
                    if 1 <= nx < n+1 and 1 <= ny < n+1:
                        if seat[nx][ny] in students[i][1:4]:
                            like += 1
                        if seat[nx][ny] == 0:
                            empty += 1
                            
                like_empty_num.append((like, empty, j, k))
        
        like_empty_num = sorted(like_empty_num, key = lambda x : (-x[0], -x[1], x[2], x[3]))
        seat[like_empty_num[0][2]][like_empty_num[0][3]] = students[i][0]
    
            
def score(input_info):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, n+1):

            count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # 교실 내에 있는지
                if (1 <= nx < n+1 and 1 <= ny < n+1):
                    if (seat[nx][ny] in input_info[seat[i][j]-1]):
                        count += 1

            # 인접한 칸에 좋아하는 학생이 있을 경우
            if (count != 0):
                sum += 10**(count-1)
    print(sum)                       

n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]
# students[i] = list(map(int, input().split()))
seat = [[0] * (n+1)  for _ in range(n+1)]
input_info = []

simulation()
input_info.sort()   
score(input_info) 
    