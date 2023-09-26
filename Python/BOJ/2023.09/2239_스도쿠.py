import sys
input = sys.stdin.readline
         
def row_check(r, num):
    # 행검사
    for x in range(9):
        if num == sudoku[r][x]:
            return False
    return True

def col_check(c, num):
    # 열검사
    for x in range(9):
        if num == sudoku[x][c]:
            return False
    return True

def box_check(r, c, num):
    # 3x3 검사
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if sudoku[nr + x][nc + y] == num:
                return False
    return True

def dfs(depth):
    if depth >= len(blank):
        for k in range(9):
            print(''.join(map(str, sudoku[k])))
        exit()

    nr, nc = blank[depth]  # 리스트에서 하나씩 튜플로 꺼낸다.
    for j in range(1, 9 + 1):
    	#dfs를 돌기전에 검사하여 조건에 맞는 것만 dfs를 돈다
        if row_check(nr, j) and col_check(nc, j) and box_check(nr, nc, j):
            sudoku[nr][nc] = j
            dfs(depth + 1)
            sudoku[nr][nc] = 0
            
sudoku = []
blank = []
for i in range(9):
    sudoku.append(list(map(int, input().rstrip())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))
            
dfs(0)