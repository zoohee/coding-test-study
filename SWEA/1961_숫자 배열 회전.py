# 시간복잡도: 
# 최악시간: 
# 난이도: D2
# Url: https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYj2mga6ZewDFASl&contestProbId=AV5Pq-OKAVYDFAUq&probBoxId=AYj2nEQ6ZfkDFASl&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5
# Reference: https://chaemi720.tistory.com/39

t = int(input())
for test in range(1, t+1):
    N = int(input())
    arr1 = [list(map(str, input().split())) for _ in range(N)]
    arr2 = [[0] * N for _ in range(N)]
    arr3 = [[0] * N for _ in range(N)]
    arr4 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr1[N-1-j][i]
            arr3[i][j] = arr1[N-1-i][N-1-j]
            arr4[i][j] = arr1[j][N-1-i]
    print("#"+str(test))
    
    for a1,a2,a3 in zip(arr2,arr3,arr4):
        a11 = ''.join(a1)
        a22 = ''.join(a2)
        a33 = ''.join(a3)
        print(a11,a22,a33) 