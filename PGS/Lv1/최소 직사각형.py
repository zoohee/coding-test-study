# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 1
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/86491
# Reference: Me
def solution(sizes):
    answer = 0
    tmp = 0
    for s in sizes:
        if s[0] < s[1]:
            tmp = s[1]
            s[1] = s[0]
            s[0] = tmp
    ver = [row[0] for row in sizes]
    hor = [row[1] for row in sizes]
    answer = max(ver)*max(hor)
    return answer

# 다른 사람 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# 치환 이렇게도 가능
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col