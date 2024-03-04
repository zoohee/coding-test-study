# 실행시간: 100ms
# 메모리: 42036KB
# 난이도: Silver 4
# Url: https://www.acmicpc.net/problem/17266
# Reference: me
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
positions = list(map(int, input().split()))

longest = 0
# 위치가 앞인 것부터 계산하기 위해 정렬
positions.sort()
for i in range(len(positions)):
    # 첫번재 가로등부터 0 인덱스까지의 거리
    if i == 0:
        longest = positions[i]-0
    # 가로등과 가로등 사이의 거리
    else:
        dist = positions[i] - positions[i-1]
        if dist % 2 == 0:
            if longest < dist // 2 :
                longest = dist // 2
        else:
            if longest < dist // 2 + 1:
                longest = dist // 2 + 1
    # 마지막 가로등은 마지막 인덱스까지의 거리도 추가로 구해주기
    if i == len(positions)-1:
        if longest < n - positions[i]:
            longest = n - positions[i]

print(longest)
