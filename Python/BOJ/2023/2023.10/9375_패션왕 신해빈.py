import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    theme = dict()
    index = 0
    clothes = []
    for _ in range(n):
        val, key = input().split()
        if key not in theme.keys():
            theme[key] = index
            clothes.append([])
            index += 1
        clothes[theme[key]].append(val)
        
    ans = 1
    for i in range(len(clothes)):
        ans *= len(clothes[i])+1

    print(ans-1)