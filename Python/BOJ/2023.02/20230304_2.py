import sys
input = sys.stdin.readline

n, k = map(int, input().split())

pre = []
nxt = []

for i in range(n):
    if i == 0:
        pre[i] = n
        nxt[i] = i + 1
    elif i == n-1:
        pre[i] = i - 1
        nxt[i] = 0
    else:
        pre[i] = i - 1
        nxt[i] = i + 1
         
# a = []
# b = []

# for i in range(n):
#     a.append(i+1)

# cnt = 0
# cursor = 0
# while a:
#     cnt += 1
#     if cnt == 3:
#         b.append(a[cursor])
#         a.remove(a[cursor])
#     cursor += 1