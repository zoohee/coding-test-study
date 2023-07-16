# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 

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
    print("#"+str(t))
    for a1,a2,a3 in zip(arr2,arr3,arr4):
        print(a1)
        a11 = ''.join(a1)
        a22 = ''.join(a2)
        a33 = ''.join(a3)
        print(a11,a22,a33) 