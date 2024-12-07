# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = [int(input()) for _ in range(n)]

max_num = m*m*n
dp = [max_num] * (n+1) # 남은 공간 제곱합 저장
dp[n] = 0

def note(index):    
    if dp[index] < max_num:        
        return dp[index]     
    
    remain = m - name[index]   
      
    for i in range(index+1, n+1):        
        if remain >= 0:            
            if i == n:                
                dp[index] = 0                
                break            
            dp[index] = min(dp[index], remain*remain+note(i))            
            remain -= name[i] + 1     
    
    return dp[index]  

print(note(0))
