#9498
import sys
input = sys.stdin.readline

score = int(input())

if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")
    
