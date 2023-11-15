import sys
input = sys.stdin.readline
# 실행 중 - 하나, 화면에 보임
# 활성화 - 보이지 않는 상태로 메모리에 직전 상태가 기록
# 비활성화 - 활성화 앱 중 메모리로부터 삭제
# A : 앱, m : 바이트 만큼의 메모리 사용 중, c : 다시 실행할 때 비용

n, m = map(int, input().split())
byte = [0]+list(map(int, input().split()))
cost = [0]+list(map(int, input().split()))
max_cost, answer = sum(cost), sum(cost)
        

# dp에는 byte값 저장 (최소cost로 M바이트 이상 확보)
dp = [[0 for _ in range(max_cost+1)] for _ in range(n+1)]
cnt = 0
for i in range(1, n+1):
    b = byte[i]
    c = cost[i]
    if c==0:
        cnt += 1
    
    for j in range(1, max_cost+1):
        if j < c: # cost 부족해서 현재 앱을 못 끄는 경우
            dp[i][j] = dp[i-1][j]
        else: # 끌 수 있을 때, 현재 앱 끈 것과 안 끈 것 비교
            dp[i][j] = max(b + dp[i-1][j-c], dp[i-1][j])
            
        if dp[i][j] >= m: # M바이트 확보 조건 충족
            answer = min(j, answer)

            
if m==0:
    print(0)
else:
    if cnt>1:
        print(answer-cnt+1)
    else:
        print(answer)
