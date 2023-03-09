#1935
import sys
input = sys.stdin.readline

n = int(input())
formula = input()
num = []
for i in range(n):
    num.append(int(input()))
    
stack = []
for i in range(len(formula)-1):
    # 첫번째 고민. 숫자를 알파벳에 맞게 어떻게 넣어주지?
    if "A" <= formula[i] and formula[i] <= "Z":
        x = num[ord(formula[i])-ord("A")]
        stack.append(x)
    else:
        b = stack.pop()
        a = stack.pop()
        if formula[i] == "*":
            stack.append(a*b)
        elif formula[i] == "+":
            stack.append(a+b)
        elif formula[i] == "-":
            stack.append(a-b)
        else:
            stack.append(a/b)
            
print(format(stack[0], ".2f"))
            