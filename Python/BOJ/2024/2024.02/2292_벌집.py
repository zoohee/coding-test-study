# 실행시간: 44ms
# 메모리: 31120KB
# 난이도: Bronze 2
# Url: https://www.acmicpc.net/problem/2292
# Reference: me

import sys
input = sys.stdin.readline

room_number = int(input())
if room_number == 1:
    print(1)
    exit(0)

cnt = 1
num = room_number-1
while(True):
    if num <= 0:
        break
    num -= 6 * cnt
    cnt += 1

print(cnt)