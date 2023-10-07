import sys
input = sys.stdin.readline

ans = set()
num = []   

def dfs():
    if num:
        ans.add(int("".join(map(str, num))))
        
    for i in range(10):
        if not num or num[-1] > i: # num이 비어 있거나 마지막 값이 더 큰 경우
            num.append(i)
            dfs()
            num.pop()

n = int(input())   
try:
    dfs()
    result = list(ans)
    result.sort()
    print(result[n - 1])
except:
    print(-1)