import sys
input = sys.stdin.readline

for i in range(int(input())):
    li = list(input())
    sum = 0
    for i in li:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
