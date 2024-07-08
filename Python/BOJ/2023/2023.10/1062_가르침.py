import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if k<5:
    print(0)
    sys.exit(0)
elif k==26:
    print(n)
    sys.exit(0)

answer = 0
words = [input().rstrip()[4:-4] for _ in range(n)]
essential = ['a', 'n', 't', 'i', 'c']
learn = [0] * 26

for c in essential:
    learn[ord(c)-ord('a')] = 1
    
def dfs(idx, cnt):
    global answer
    
    if cnt == k-5:
        read = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                read += 1
        answer = max(answer, read)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

dfs(0, 0)
print(answer)

