n = int(input())

paper = [[False]*100 for _ in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = True

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            cnt += 1

print(cnt)
