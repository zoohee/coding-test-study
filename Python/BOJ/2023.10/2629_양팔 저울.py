import sys
input = sys.stdin.readline

n = int(input())
chu = list(map(int, input().split()))
m = int(input())
marble = list(map(int, input().split()))

dp = [0]

for c in chu:
    tmp = []
    for i in dp:
        tmp.append(i+c) # 구슬 판 반대 판에 추 무게 더한 것 추가
        tmp.append(abs(i-c)) # 추 뺀 것 추가 (구슬과 같은 판에 올라감)
    dp = list(set(dp+tmp)) # 추로 계산할 수 있는 무게가 전부 dp에 담김
    
print(dp)
for m in marble:
    print('Y' if m in dp else 'N',end=' ')