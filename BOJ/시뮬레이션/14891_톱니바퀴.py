# 시간복잡도: 
# 최악시간: 
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/14891
# Reference: 
import sys
input = sys.stdin.readline
from collections import deque

wheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    n = n - 1
    lr = []
    # 값 미리 저장 안해두면 wheel 돌리면서 값 체크 못함
    for i in range(4):
        lr.append([wheels[i][6], wheels[i][2]])
        
    if n != 0:
        for i in range(n, 0, -1):
            if lr[i][0] != lr[i-1][1]:
                if (n-(i-1)) % 2 == 0:
                    wheels[i-1].rotate(d)
                else:
                    wheels[i-1].rotate(-d)
            else:
                break
    if n != 3:
        for i in range(n, 3):
            if lr[i][1] != lr[i+1][0]:
                if (n-(i+1)) % 2 == 0:
                    wheels[i+1].rotate(d)
                else:
                    wheels[i+1].rotate(-d)
            else:
                break
    wheels[n].rotate(d)
    
    # for wheel in wheels:
    #     print(wheel)
    # print("---------------")
       
            
                
                
# for i in range(n):
#     num, direction = map(int, input().split())
#     num = num - 1
#     step = 0
#     if direction == -1:
#         if num == 0:
#             while(right_check(num+step, num+1+step)):
#                 print(step)
#                 step += 1 
#             for i in range(step):
#                 if i % 2 == 0:
#                     wheels[num+1+i] = clockwise(wheels[num+1+i])
#                 else:
#                     wheels[num+1+i] = anti_clockwise(wheels[num+1+i])
#             wheels[num] = anti_clockwise(wheels[num])
#         elif num == 1 or num == 2:
#             if left_check(num, num-1):
#                 wheels[num-1] = clockwise(wheels[num-1])
#             if right_check(num, num+1):
#                 wheels[num+1] = clockwise(wheels[num+1])
#             wheels[num] = anti_clockwise(wheels[num])
#         else:
#             if left_check(num, num-1):
#                 wheels[num-1] = clockwise(wheels[num-1])
#             wheels[num] = anti_clockwise(wheels[num])
#     else:
#         if num == 0:
#             if right_check(num, num+1):
#                 wheels[num+1] = anti_clockwise(wheels[num+1])
#             wheels[num] = clockwise(wheels[num])
#         elif num == 1 or num == 2:
#             if left_check(num, num-1):
#                 wheels[num-1] = anti_clockwise(wheels[num-1])
#             if right_check(num, num+1):
#                 wheels[num+1] = anti_clockwise(wheels[num+1])
#             wheels[num] = clockwise(wheels[num])
#         else:
#             if left_check(num, num-1):
#                 wheels[num-1] = anti_clockwise(wheels[num-1])
#             wheels[num] = clockwise(wheels[num])

answer = 0
for i in range(len(wheels)):
    answer += (2**i) * wheels[i][0]
print(answer)