# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 3
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/12987
# Reference: Me

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    check = 0
    for i in range(len(B)):
        for j in range(check, len(B)):
            if B[i] > A[j]:
                answer += 1
                check = j+1
                break
        if j==len(B)-1:
            return answer
                
    return answer

# 뇨뇽 코드
# def solution(A, B):
#     answer = 0
#     A.sort(reverse = True)
#     B.sort(reverse = True)
#     i = 0
#     for a in A:
#         if a < B[i]:
#             answer += 1
#             i += 1
#     return answer