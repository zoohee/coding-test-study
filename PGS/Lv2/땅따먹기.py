# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/12913
# Reference: Me
def solution(land):
    answer = 0
    dp = [[0]*4 for _ in range(len(land))]
    dp[0] = land[0]
    
    for i in range(1, len(land)):
        for j in range(4):
            max_value = 0
            for k in range(4):
                if dp[i-1][k]+land[i][j] > max_value and j != k:
                    dp[i][j] = dp[i-1][k] + land[i][j]
                    max_value = dp[i][j]
    
    answer = max(dp[-1])
    return answer

# 다른 사람 풀이
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
