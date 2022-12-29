#1267
import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int,input().split()))
Y = 0
M = 0

for i in range(len(cost)):
    Y += (int(cost[i]/30)+1)*10
    M += (int(cost[i]/60)+1)*15
    
if Y == M:
    print("Y", "M", Y, sep=' ')
elif Y > M:
    print("M", M, sep=' ')
else:
    print("Y", Y, sep=' ')
