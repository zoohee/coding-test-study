import sys
input = sys.stdin.readline

n = int(input())
superior = list(map(int, input().split()))

# 트리 만들기
tree = [[] for _ in range(n)]
for i in range(1, n):
    tree[superior[i]].append(i)
    
time = [0] * n


def dp(v):
    child = []
    # underling 부하 직원들
    for u in tree[v]:
        dp(u)
        # 걸리는 시간 저장
        child.append(time[u])
    if not tree[v]:
        child.append(0)
    
    # 시간 오래 걸리는 순으로 정렬
    child.sort(reverse=True)
    need_time = [child[i]+i+1 for i in range(len(child))]
    time[v] = max(need_time)
    print(child)

dp(0)
print(time[0]-1)