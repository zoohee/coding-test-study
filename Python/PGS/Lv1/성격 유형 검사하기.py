# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 1
# Url: https://www.acmicpc.net/problem/
# Reference: Me
def solution(survey, choices):
    answer = ''
    score = [3, 2, 1, 0, 1, 2, 3]
    mbti = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
    for i in range(len(survey)):
        if choices[i] >= 1 and choices[i] <= 3:
            mbti[survey[i][0]] += score[choices[i]-1]
        else:
            mbti[survey[i][1]] += score[choices[i]-1]
    
    if mbti["R"] >= mbti["T"]:
        answer += 'R'
    else:
        answer += 'T'
    if mbti["C"] >= mbti["F"]:
        answer += 'C'
    else:
        answer += 'F'
    if mbti["J"] >= mbti["M"]:
        answer += 'J'
    else:
        answer += 'M'
    if mbti["A"] >= mbti["N"]:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer