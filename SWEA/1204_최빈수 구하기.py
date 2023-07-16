# 시간복잡도: 
# 최악시간: 
# 난이도: D2
# Url: https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AV13zo1KAAACFAYh&categoryId=AYj2nEQ6ZfkDFASl&categoryType=BOX
# Reference: Me

t = int(input())

for test in range(1, t+1):
    answer = 0
    arr = [0] * 101
    n = int(input())
    score = list(map(int, input().split()))
    for i in range(len(score)):
        arr[score[i]] += 1
    max_score = max(arr)
    for j in range(100, 0, -1):
        if max_score <= arr[j]:
            answer = j
            break
    print("#"+str(test)+" "+str(answer))