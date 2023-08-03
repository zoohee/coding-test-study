#2446
n = int(input())

for i in range(n):
    print(i * " " + (2*(n-i)-1) * "*")
for i in range(n-1):
    print((n-2-i) * " " + (2*i+3) * "*")