sugar = int(input())

bag = 0
while sugar >=0:
    if sugar % 5 == 0: #5의 배수
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1 #5의 배수가 될때까지 설탕-3 봉지+1
else:
    print(-1)