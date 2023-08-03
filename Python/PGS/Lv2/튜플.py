# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/64065
# Reference: Me
def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s_sorted = sorted(s, key = lambda x :len(x))
    tmp = []
    str_answer = []
    
    for i in range(len(s_sorted)):
        tmp = s_sorted[i].split(',')
        tmp = [x for x in tmp if x not in str_answer]
        str_answer.append(tmp[0])
        answer.append(int(tmp[0]))
        
    return answer