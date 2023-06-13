# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/14888
# Reference: 
# 아래 코드는 답이 잘 나오지만 시간초과 뜨는 코드
# DFS로 다시 구현해볼것
import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
operator_input = list(map(int, input().split()))
operator_list = ['+', '-', '×', '÷']
operator = []
for i in range(len(operator_input)):
    for j in range(operator_input[i]):
        operator.append(operator_list[i])
            
tmp = 0
min_answer = 1e9
max_answer = -1e9
per = list(permutations(operator))
sorted(set(per), key = lambda x: per.index(x))
for o in per:
    tmp = num[0]
    for i in range(1, N):
        if o[i - 1] == '+':
            tmp += num[i]
        elif o[i - 1] == '-':
            tmp -= num[i]
        elif o[i - 1] == '*':
            tmp *= num[i]
        elif o[i - 1] == '/':
            tmp = int(tmp / num[i])
    min_answer = min(min_answer, tmp)
    max_answer = max(max_answer, tmp)
    
print(max_answer)
print(min_answer)