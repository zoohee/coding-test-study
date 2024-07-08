import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
    
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)
    
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF",  end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
print("\n")
   
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    print(k)
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] >= INF:
                print("INF",  end=" ")
            else:
                print(graph[a][b], end=" ")
        print()
    print("\n")
    
 
# 5
# 10
# 1 2 5
# 1 4 3
# 2 5 4
# 3 4 1
# 3 5 2
# 4 1 -1
# 4 5 -1
# 5 2 -2
# 5 3 3
# 5 4 2
