import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = [[0,0] for _ in range(6)]

for i in range(n):
    s, y = map(int, input().split())
    students[y-1][s] += 1

answer = 0

for grade in students:
    for sex in grade:
        answer +=  sex // k
        if sex % k != 0:
            answer += 1

print(answer)
        
    
