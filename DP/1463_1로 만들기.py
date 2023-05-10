# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/1463
# Reference: https://jae04099.tistory.com/199
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)

# 1을 빼는 경우, 2로 나누는 경우, 3으로 나누는 경우
# 모든 경우의 수 중 최소값을 찾아내야 한다.
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[n])