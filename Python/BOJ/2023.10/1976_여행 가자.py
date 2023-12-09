import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

n = int(input())
m = int(input())

parents = [i for i in range(n)]
for i in range(n):
    city = list(map(int,input().split()))
    for j in range(n):
        if city[j] == 1:
            union(i,j)
            print(parents)

parents = [-1] + parents
plan = list(map(int,input().split()))
start = parents[plan[0]]
for i in range(1,m):
    if parents[plan[i]] != start:
        print("NO")
        break
else:
    print("YES")

