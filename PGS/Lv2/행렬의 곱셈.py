# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            for j in range(len(arr2)):
                answer[i][k] += arr1[i][j] * arr2[j][k]
                
    return answer

# 다른 사람 풀이
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]