import sys 
input = sys.stdin.readline

a, b = map(int, input().split())

temp = []
for i in range( 1, b + 1):
    for j in range(i):
        temp.append(i)

print(sum(temp[a - 1:b]))

