# 시간복잡도: 
# 최악시간: 
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/14891
# Reference: https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-14891-%ED%95%B4%EC%84%A4-python-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B4
import sys
input = sys.stdin.readline
from collections import deque

wheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    n = n - 1
    lr = []
    # 값 미리 저장 안해두면 wheel 돌리면서 값 체크 못함
    for i in range(4):
        lr.append([wheels[i][6], wheels[i][2]])
        
    if n != 0:
        for i in range(n, 0, -1):
            if lr[i][0] != lr[i-1][1]:
                if (n-(i-1)) % 2 == 0:
                    wheels[i-1].rotate(d)
                else:
                    wheels[i-1].rotate(-d)
            else:
                break
    if n != 3:
        for i in range(n, 3):
            if lr[i][1] != lr[i+1][0]:
                if (n-(i+1)) % 2 == 0:
                    wheels[i+1].rotate(d)
                else:
                    wheels[i+1].rotate(-d)
            else:
                break
    wheels[n].rotate(d)

answer = 0
for i in range(len(wheels)):
    answer += (2**i) * wheels[i][0]
print(answer)