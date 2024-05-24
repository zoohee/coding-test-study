# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, h = map(int, input().split())
cave = [int(input()) for _ in range(n)]
# 아래>위>아래>위

print("===============")
# 높이만큼 시작 (아래에서 위로)
for i in range(h):
    count = 0
    for j in range(n):
        if (j+1)%2 != 0:
            if j - cave[j] < 0:
                count += 1
        else:
            if j - (h - cave[j]) > 0:
                count += 1
    print(count)