#2841
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
stack = [[] for i in range(7)]
answer = 0

for i in range(n):
    cnt = 1
    line, plat = map(int, input().split())
    # 스택이 비어있지 않고 pop 값보다 plat이 작거나 같으면
    while(len(stack[line]) != 0 and plat <= stack[line][-1]):
        if stack[line][-1] == plat:
            cnt -= 1
        else:
            cnt += 1
        stack[line].pop()
    
    stack[line].append(plat)
    answer += cnt
        
    # if not stack[line]:
    #     stack[line].append(plat)
    #     cnt += 1
    # else:
    #     print(i, ":", stack[line][-1])
    #     # 마지막 값이 더 적을 때
    #     if stack[line][-1] < plat:
    #         stack[line].append(plat)
    #         cnt += 1
    #     #마지막 값이 같을때
    #     elif stack[line][-1] == plat:
    #         continue
    #     #마지막 값이 더 클 때
    #     else:
    #         while(stack[line][-1] > plat):
    #             # 비어있는 경우 체크해줘야 함.
    #             stack[line].pop()
    #             cnt += 1
    #             if not stack[line]:
    #                 break
    #         stack[line].append(plat)
    #         cnt += 1
# 마지막 값이 더 작아질 때까지 pop해줘야하는데 오류
             
print(answer)