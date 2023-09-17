# 시간초과 -> 블로그 참고

import heapq

n = int(input())
for _ in range(n):
    min_que = []
    max_que = []
    
    m = int(input())
    visited = [False]*m
    
    for i in range(m):
        order, num_s = input().split()
        num = int(num_s)
        if(order == 'I'):
            heapq.heappush(min_que, (num, i))
            heapq.heappush(max_que, (-num, i))
            visited[i] = True
        else:
            if(num == -1): #최소힙
                while min_que and not visited[min_que[0][1]]:
                    heapq.heappop(min_que)
                if min_que:
                    visited[min_que[0][1]] = False
                    heapq.heappop(min_que)
            else: #최대힙
                while max＿que and not visited[max＿que[0][1]]:
                    heapq.heappop(max＿que)
                if max_que:                
                    visited[max_que[0][1]] = False
                    heapq.heappop(max_que)
        print(min_que)
        print(max_que)     
                    
    while min_que and not visited[min_que[0][1]]:
        heapq.heappop(min_que)
    while max_que and not visited[max_que[0][1]]:
        heapq.heappop(max_que)   
          
    if(max_que and min_que):
        print(-max_que[0][0], min_que[0][0])
    else:
        print("EMPTY")

                