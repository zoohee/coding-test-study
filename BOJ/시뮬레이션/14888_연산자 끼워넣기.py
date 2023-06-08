# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline
from itertools import permutations
from collections import deque

def operation(a, b, o):
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '×':
        return a*b
    else:
        if a < 0:
            a = abs(a)
            return -(a//b)
        else:
            return a//b

N = int(input())
num = list(map(int, input().split()))
operator_input = list(map(int, input().split()))
operator = []
for i in range(len(operator_input)):
    for j in range(operator_input[i]):
        if i == 0:
            operator.append('+')
        elif i == 1:
            operator.append('-')
        elif i == 2:
            operator.append('×')
        else:
            operator.append('÷')
            
tmp = 0
min_answer = 1e9
max_answer = -1e9
per = list(permutations(operator))
sorted(set(per), key = lambda x: per.index(x))
for o in per:
    formula = deque()
    for i in range(len(o)):
        formula.append(num[i])
        formula.append(o[i])
    formula.append(num[-1])
    
    while(True):
        if len(formula) == 1:
            break
        tmp = operation(formula[0], formula[2], formula[1])
        for i in range(3):
            formula.popleft()
        formula.appendleft(tmp)

    min_answer = min(min_answer, formula[0])
    max_answer = max(max_answer, formula[0])
    
print(max_answer)
print(min_answer)