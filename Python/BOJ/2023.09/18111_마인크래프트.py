import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

block = [list(map(int, input().split())) for _ in range(N)]

answer = sys.maxsize
index = 0
for floor in range(257):
    exceed, lack = 0, 0
    
    for i in range(N):
        for j in range(M):
            if block[i][j] > floor:
                exceed += block[i][j] - floor # 현재 층보다 많음
            else:
                lack += floor - block[i][j] # 현재 층보다 적음
    if lack > exceed + B: # 창고블록+해당층에서 집어넣는 블록보다 쌓을 블록이 크면 못함
        continue
    
    if exceed * 2 + lack <= answer: # 더 최소시간이면
        answer = exceed * 2 + lack
        index = floor

print(answer, index)
    