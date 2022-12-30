#2439
n = int(input())

for i in range(n):
    star = ""
    for j in range(n-i-1):
        star += " "
    for j in range(i+1):
        star += "*"
    print(star)