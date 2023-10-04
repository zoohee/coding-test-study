INF = int(1e9)
T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    n = arr[0]
    graph = [[INF]*(n+1) for _ in range(n+1)]
    index = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[index] == 0:
                graph[i][j] = INF
            else:
                graph[i][j] = arr[index]
            index += 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    answer = INF
    for i in range(1, n+1):
        tmp = 0
        for j in range(1, n+1):
            if graph[i][j] < INF:
                tmp += graph[i][j]
        answer = min(tmp, answer)

    print("#",t," ",answer, sep="")