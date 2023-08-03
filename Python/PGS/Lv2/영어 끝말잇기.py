# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=python3
# Reference: Me+Study
def solution(n, words):
    words_set = set()
    words_set.add(words[0])
    
    # set: O(1) list:O(n)
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words_set:
            return [(i%n)+1, (i//n)+1]
        words_set.add(words[i])
        
    return [0, 0]