# 실행시간: 136ms
# 메모리: 31252KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/19941
# Reference: me
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hbg = list(input().rstrip())

ans = 0
check = False
for i in range(len(hbg)):
    
    if hbg[i] == 'P':
        for j in range(-k, k+1):
            if j==0:
                continue
            if i+j>=0 and i+j<len(hbg):
                if hbg[i+j] == 'H':
                    hbg[i+j] = 'A'
                    ans += 1
                    check = True
                    break

print(ans)

        
    