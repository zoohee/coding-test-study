def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for x, y in puddles: # 웅덩이면 -1 표시
        dp[y][x] = -1
    
    dp[1][1] = 1 # 시작점
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] != -1: # 웅덩이 아니면 왼+위에서 오는거 저장
                dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            else: # 웅덩이면 0으로 표시해서 다음거에 영향 안가게
                dp[i][j] = 0
    return dp[n][m]