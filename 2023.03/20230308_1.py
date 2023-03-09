#2493
import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int,input().split()))
laser = []

for i in range(len(tower)):
    if laser:
        while(laser):
            if tower[i] > laser[-1][0]:
                laser.pop()
                if not laser:
                    print(0, end=" ")
            else:
                print(laser[-1][1]+1, end=" ")
                # laser.pop()
                break
        laser.append([tower[i], i])
    else:
        print(0, end=" ")
        laser.append([tower[i], i])









# mark = False

# for i in range(n):
#     pop = tower.pop()
#     for j in range(len(tower)):
#         if tower[len(tower) - 1 - j] > pop:
#             laser.append(len(tower) - 1 - j + 1)
#             mark = True
#             break
#     if not mark:
#         laser.append(0)
#     mark = False

# for i in range(n):
#     print(laser[n-1-i], end=" ")
    
# 처음에 레이저에 맞을 수 있는 탑의 개수인줄 알았는데
# 레이저를 수신한 탑의 "번호" 출력이었다.