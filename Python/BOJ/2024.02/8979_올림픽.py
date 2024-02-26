# 실행시간: 44ms
# 메모리: 31120KB
# 난이도: Silver 5
# Url: https://www.acmicpc.net/problem/8979
# Reference: me

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

medal = [list(map(int, input().split())) for _ in range(n)]

medal.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

index = 0
check = False
for i in range(n):
    if medal[i][0] == k:
        index = i
        for j in range(i-1, -1, -1):
            if (medal[i][1], medal[i][2], medal[i][3]) == (medal[j][1], medal[j][2], medal[j][3]):
                index = j
            else:
                check = True
                break
        
        if check:
            break

print(index+1)
