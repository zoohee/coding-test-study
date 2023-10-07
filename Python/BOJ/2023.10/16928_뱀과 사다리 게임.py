from collections import deque

def bfs():
    que = deque([1])
    visited[1] = True
    while que:
        now = que.popleft()
        # 1~6 이동
        for move in range(1,7):
            check_move = now+move # 현재 위치 + 주사위값
            if 0 < check_move <= 100 and not visited[check_move]:
                # 사다리나 뱀 중에 있으면
                if check_move in ladder.keys():
                    check_move = ladder[check_move] 
                elif check_move in snake.keys():
                    check_move = snake[check_move]

                # 사다리나 뱀을 타고간 위치로 변경되었을 때 방문하지 않은 위치거나
                # 사다리나 뱀을 타지 않았으면
                if not visited[check_move]:
                    que.append(check_move)
                    visited[check_move] = True
                    board_cnt[check_move] = board_cnt[now] + 1 # 이동 횟수
                    
N, M = map(int,input().split())
board_cnt = [0] * 101
visited = [False] * 101

snake = dict()
ladder = dict()

for _ in range(N):
    i,j = map(int,input().split())
    ladder[i] = j
for _ in range(M):
    i,j = map(int,input().split())
    snake[i] = j

bfs()
print(board_cnt[100])