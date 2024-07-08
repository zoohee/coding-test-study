#5397
#키로거
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    answer = deque()
    tmp = deque()
    test_case = input().rstrip()
    
    for j in range(len(test_case)):
        if test_case[j] == '<':
            if len(answer) != 0:
                tmp.append(answer.pop())
        elif test_case[j] == '>':
            if len(tmp) != 0:
                answer.append(tmp.pop())
        elif test_case[j] == '-':
            if len(answer) != 0:
                answer.pop()
        else:
            answer.append(test_case[j])
            while(tmp): 
                answer.append(tmp.pop())
    
    # for문 돌리고 나서 
    while(tmp): 
        answer.append(tmp.pop())
    
    answer_string = []
    while(answer):
        answer_string.append(answer.popleft())
        
    print("".join(answer_string))
    
# 링크드리스트가 시간복잡도가 더 짧음