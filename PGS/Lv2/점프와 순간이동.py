# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/12980
# Reference: Me
def solution(n):
    ans = 1
    while (True):
        if (n == 1):
            return ans
        if (n%2 != 0):
            n -= 1
            ans += 1
        n = n // 2
    return ans