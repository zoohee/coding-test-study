# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/17684
# Reference: https://hbj0209.tistory.com/89

def solution(msg):
    answer = []
    dict = {chr(i + 64): i for i in range(1, 27)}
    cnt = 27
    i = 0
    search = ''
    
    while i< len(msg):
        search += msg[i]
        if search in dict:
            i += 1
        else:
            dict[search] = cnt
            cnt += 1
            s = search[:-1]
            answer.append(dict[s])
            search = ''
    
    answer.append(dict[search])
    return answer