# 시간복잡도: 
# 최악시간: 
# 난이도: D2
# Url: https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYj2mga6ZewDFASl&contestProbId=AXuARWAqDkQDFARa&probBoxId=AYj2nEQ6ZfkDFASl&type=USER&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5
# Reference: https://tarra.tistory.com/entry/SW-Expert-Academy-12712-%ED%8C%8C%EB%A6%AC%ED%87%B4%EC%B9%983

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