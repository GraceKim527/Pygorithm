import sys
input = sys.stdin.readline

n = int(input())

fibonacci = []
num = 0
for i in range(n + 1):
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(num)

print(fibonacci[-1])