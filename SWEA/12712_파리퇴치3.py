# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: 
# Reference: 
import sys
input = sys.stdin.readline

t = int(input())

dw = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dy = [-1, 1, 1, -1]
dz = [1, 1, -1, -1]

for test in range(t):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    tmp = 0
    for i in range(n):
        for j in range(n):
            answer1 = graph[i][j]
            answer2 = graph[i][j]
            for k in range(1, m):
                for l in range(4):
                    nw = i + k * dw[l]
                    nx = j + k * dx[l]
                    ny = i + k * dy[l]
                    nz = j + k * dz[l]
                    
                    if -1 < nw < n and -1 < nx < n:
                        answer1 += graph[nw][nx]
                    if -1 < ny < n and -1 < nz < n:
                        answer2 += graph[ny][nz]
            tmp = max(answer1, answer2)
            answer = max(tmp, answer)
    print("#"+str(test+1)+" "+str(answer))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # answer = 0
    # center = n//2
    # answer1 = graph[center][center]
    # answer2 = graph[center][center]
    # print(answer1)
    # for i in range(m):
    #     w, x, y, z = center
    #     for j in range(4):
    #         nw = w + (i+1) * dw[j]
    #         nx = x + (i+1) * dx[j]
    #         answer1 += graph[nw][nx]
    #         print(answer1)
    #         answer2 += graph[center+dy[j]][center+dz[j]]

    