# 실행시간: 40 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/7682
# Reference: 

import sys
input = sys.stdin.readline

def check(board, type):
    if board[0] == type and board[0] == board[1] == board[2]:
        return True
    elif board[0] == type and board[0] == board[3] == board[6]:
        return True
    elif board[4] == type and board[1] == board[4] == board[7]:
        return True
    elif board[4] == type and board[3] == board[4] == board[5]:
        return True
    elif board[8] == type and board[6] == board[7] == board[8]:
        return True
    elif board[8] == type and board[2] == board[5] == board[8]:
        return True
    elif board[4] == type and board[0] == board[4] == board[8]:
        return True
    elif board[4] == type and board[2] == board[4] == board[6]:
        return True
    else:
        return False

while True:
    board = input().rstrip()
    if board == "end":
        break
    
    x = board.count('X')
    o = board.count('O')
    
    if x == o+1 or x == o: 
        if x == o+1:
            result_one = check(board, 'X')
            result_two = check(board, 'O')
            
        elif x == o:
            result_one = check(board, 'O')
            result_two = check(board, 'X')
        
        if result_two:
            print("invalid")
            
        elif not result_one:
            if board.count('.') == 0:
                print("valid")
            else:
                print("invalid")
        else:
            print("valid")
    
    else:
        print("invalid")
    