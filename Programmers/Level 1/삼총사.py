from itertools import combinations

def solution(number):
    nums = list(combinations(number,3))
    
    cnt = 0
    for num in nums:
        if sum(num) == 0:
            cnt += 1
    return cnt