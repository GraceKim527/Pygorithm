import sys 
input = sys.stdin.readline

li = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        li.append(n)

if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)