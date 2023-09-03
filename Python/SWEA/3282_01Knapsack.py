# https://sskl660.tistory.com/88
import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    zero = [[0, 0]]
    tmp = [list(map(int, input().split())) for _ in range(N)]
    things = zero + tmp

    dp = [0]*(K+1)
    
    for i in range(1, N+1):
        for j in range(K, things[i][0]-1, -1): # K개의 부피부터 현재 부피까지
            dp[j] = max(things[i][1] + dp[j-things[i][0]], dp[j]) # (현재 가치 + 더할 수 있는 가치) vs 현재 최대 가치
   
    print("#"+str(t)+" "+str(dp[K]))
    
