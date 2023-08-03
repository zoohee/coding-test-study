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

# from sys import stdin
# n = int(stdin.readline().strip())
# height = [100000001]+list(map(int,stdin.readline().strip().split()))
# num = [0 for i in range(n+1)]
# for i in range(1,n+1):
#     standard = i-1
#     while(height[standard]<height[i]):
#         standard = num[standard]
#     num[i] = standard
# num.pop(0)
# print(' '.join(map(str,num)))

    
# 처음에 레이저에 맞을 수 있는 탑의 개수인줄 알았는데
# 레이저를 수신한 탑의 "번호" 출력이었다.