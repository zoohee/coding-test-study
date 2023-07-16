# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# Reference: 

t = int(input())
for test in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = -999999
    if len(a) < len(b):
        for i in range(m-n+1):
            tmp = 0
            for j in range(i, i+len(a)):
                print(a[j-i]*b[j])
                tmp += a[j-i]*b[j]
            print(tmp)
            answer = max(answer, tmp)
    # else:
    #     for i in range(n-m+1):
    #         for j in range(len(b)):
    #             tmp += a[j]*b[j]
    #         answer = max(answer, tmp)
    print("#"+str(test)+" "+str(answer))
    