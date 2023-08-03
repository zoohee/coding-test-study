# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/76502
# Reference: Me
# deque에 rotate라는 함수가 있었음..
from collections import deque

def rotate(s):
    tmp = s.popleft()
    s.append(tmp)
    return s

def valid(s):
    stack = []
    if s[0] == ')' or s[0] == ']' or s[0] == '}':
        return False
    
    stack.append(s[0])
    for i in range(1, len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            if stack[-1] == '(' and s[i] == ')':
                stack.pop()
            elif stack[-1] == '{' and s[i] == '}':
                stack.pop()
            elif stack[-1] == '[' and s[i] == ']':
                stack.pop()
    
    if len(stack) != 0:
        return False
    else:
        return True
    
def solution(s):
    answer = 0
    deq = deque()
    
    for i in range(len(s)):
        deq.append(s[i])
        
    for i in range(len(s)):
        if valid(deq):
            answer += 1
        rotate(deq)

    return answer