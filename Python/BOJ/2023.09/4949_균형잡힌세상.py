from collections import deque 
import sys
input = sys.stdin.readline

stack = deque()
        
while(True):
    s = input()
    if s[0]=='.':
        break
    for i in range(len(s)):
        if(s[i]=='[' or s[i]=='('):
            stack.append(s[i])
            
        elif(s[i]==']' or s[i]==')'):
            if(len(stack) != 0):
                if s[i]==']' and stack[-1]=='[':
                    stack.pop()
                elif s[i]==')' and stack[-1]=='(':
                    stack.pop()
                else:
                    print("no")
                    stack.clear()
                    break
            else:
                print("no")
                stack.clear()
                break
                
        elif(s[i]=='.'):
            if(len(stack) == 0):
                print("yes")
            else:
                print("no")
                stack.clear()    