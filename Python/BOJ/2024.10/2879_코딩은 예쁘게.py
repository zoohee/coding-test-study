# 실행시간: 44 ms
# 메모리: 31120 KB
# 난이도: Gold 3
# Url: https://www.acmicpc.net/problem/2879
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
cur = list(map(int, input().split()))
tab = list(map(int, input().split()))
diff = [cur[i] - tab[i] for i in range(n)]

cnt = 0
for i in range(n):
    if diff[i] == 0:
        continue

    x = 1 if diff[i] > 0 else -1
    
    while diff[i] != 0:
        cnt += 1
        for j in range(i, n):
            if diff[j]*x <= 0: # 음수면 양수, 양수면 음수일때 멈춤
                break
            diff[j] -= x # 그룹으로 묶어서 탭 맞추기

print(cnt)