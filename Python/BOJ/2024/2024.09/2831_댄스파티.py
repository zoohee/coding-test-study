# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
# 양수 : 키가 큰 여자
# 음수 : 키가 작은 여자
men = list(map(int, input().split()))
women = list(map(int, input().split()))
men.sort()
women.sort()

answer = 0
s = 0
e = n-1
while s < n and 0 <= e:
    if men[s] < 0 and 0 < women[e] and abs(men[s]) > women[e]:
        answer += 1
        s += 1
        e -= 1
    elif men[s] < 0 and 0 < women[e] and abs(men[s]) <= women[e]:
        e -= 1
    elif 0 < men[s] and women[e] < 0 and men[s] < abs(women[e]):
        answer += 1
        s += 1
        e -= 1
    elif 0 < men[s] and women[e] < 0 and men[s] >= abs(women[e]):
        e -= 1
    elif men[s] < 0 and women[e] < 0:
        s += 1
    elif 0 < men[s] and 0 < women[e]:
        e -= 1

print(answer)
    