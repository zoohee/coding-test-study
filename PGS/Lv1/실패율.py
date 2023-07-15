# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 1
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/42889
# Reference: 
def solution(N, stages):
    People = len(stages)
    faillist = {}
    
    for i in range(1, N + 1):
        if People != 0:
            cnt = stages.count(i)
            faillist[i] = cnt / People
            People -= cnt
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)