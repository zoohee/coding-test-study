# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/84512
# Reference: https://velog.io/@ehddms7410/Algo-%EA%B5%AC%ED%98%84-50%EB%AC%B8%EC%A0%9C#1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4---%EB%AA%A8%EC%9D%8C%EC%82%AC%EC%A0%84
import itertools

def solution(word):
    word = [w for w in word]
    answer = []
    for n in range(1,6):
        answer += [list(item) for item in list(itertools.product((['A', 'E', 'I', 'O', 'U']), repeat=n))]
    answer = sorted(answer)
    return answer.index(word) + 1