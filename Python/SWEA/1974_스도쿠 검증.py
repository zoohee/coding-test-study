# 시간복잡도: 
# 최악시간: 
# 난이도: D2
# Url: https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYj2mga6ZewDFASl&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AYj2nEQ6ZfkDFASl&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5
# Reference: Me
t = int(input())
for test in range(1, t+1):
    answer = 1
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        row = [0] * 9
        col = [0] * 9
        for j in range(9):
            row[j] = sudoku[i][j]
            col[j] = sudoku[j][i]
        if len(row) != len(set(row)):
            answer = 0
        if len(col) != len(set(col)):
            answer = 0
    if answer == 1:
        for i in [0, 3, 6]:
            square = [0] * 9
            for j in [0, 3, 6]:
                index = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        square[index] = sudoku[k][l]
                        index += 1
                if len(square) != len(set(square)):
                    answer = 0
    print("#"+str(test)+" "+str(answer))
    
    