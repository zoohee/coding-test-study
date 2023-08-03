# 시간복잡도: 
# 최악시간: 
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/15686
# Reference: https://codesyun.tistory.com/185
import sys
input = sys.stdin.readline
from itertools import combinations

def chicken_distance():
    answer = 1000000
    # 이차원 배열 값 넣어서 초기화
    # distance = [[0] * len(chicken) for _ in range(len(house))]
    # 치킨집 두개를 뽑아서 집과의 거리를 각각 다 구하고
    # 최솟값 저장.
    for c in combinations(chicken, M):
        temp = 0
        for h in house:
            distance = 100000
            # 집 두개면 두번 순회
            for j in range(M):
                distance = min(distance, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
            temp += distance
        answer = min(answer, temp)
    return answer

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

print(chicken_distance())