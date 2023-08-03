# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/12953
# Reference: chatGPT
import math
def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = (answer * arr[i]) // math.gcd(answer, arr[i])
    return answer