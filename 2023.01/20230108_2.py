#13300
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

girls = [0] * 6
boys = [0] * 6
cnt = 0

for i in range(n):
    s, g = map(int, input().split()) # 성별 학년
    if s == 0: # 여학생
        girls[g-1] += 1
    else: # 남학생
        boys[g-1] += 1
print(girls)
print(boys)
for i in range(len(girls)):
    if girls[i] != 0:
        cnt += int(girls[i] / k) + int(girls[i] % k)
for i in range(len(boys)):
    if boys[i] != 0:    
        cnt += int(boys[i] / k) + int(boys[i] % k)
    
print(cnt)