# 실행시간: 148ms
# 메모리: 38340KB
# 난이도: Silver 4
# Url: https://www.acmicpc.net/problem/20125
# Reference: me
import sys
input = sys.stdin.readline

n = int(input())
cookie = [list(input()) for _ in range(n)]

heart = ()
check = False
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            heart = (i+1, j)
            check = True
            break
    if check:
        break

body = [0, 0, 0, 0, 0]

# 왼쪽 팔
j = heart[1]-1
while(j>=0):
    if cookie[heart[0]][j] == '*':
        body[0] += 1
        j -= 1
    else:
        break

# 오른쪽 팔
j = heart[1]+1
while(j<=n-1):
    if cookie[heart[0]][j] == '*':
        body[1] += 1
        j += 1
    else:
        break

# 허리
i = heart[0]+1
while(i<=n-1):
    if cookie[i][heart[1]] == '*':
        body[2] += 1
        i += 1
    else:
        break

waist = i-1

# 왼쪽 다리
i = waist + 1
while(i<=n-1):
    if cookie[i][heart[1]-1] == '*':
        body[3] += 1
        i += 1
    else:
        break

# 오른쪽 다리
i = waist + 1
while(i<=n-1):
    if cookie[i][heart[1]+1] == '*':
        body[4] += 1
        i += 1
    else:
        break

print(heart[0]+1, heart[1]+1)
for i in range(5):
    print(body[i], end =" ")
