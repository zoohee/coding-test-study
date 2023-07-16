# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AV13zo1KAAACFAYh&categoryId=AYj2nEQ6ZfkDFASl&categoryType=BOX
# Reference: 

t = int(input())
arr = [0] * 101
answer = 0

for test in range(1, t+1):
    n = int(input())
    score = list(map(int, input().split()))
    for i in range(len(score)):
        arr[score[i]] += 1
        print(arr)
    max_score = max(arr)
    for j in range(100, 0, -1):
        if max_score <= arr[j]:
            answer = j
            break
    print("#"+str(test)+" "+str(answer))