# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/2623
# Reference: 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = list(map(input().split()))
numbers = []
for i in range(1, int(k[0])):
    numbers.append(int(k[i]))
    
print(numbers)