import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trueman = set(input().split()[1:])


party = []
for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p & trueman:
            trueman = trueman.union(p)

ans = 0

for p in party:
    if p & trueman:
        continue
    ans += 1

print(ans)