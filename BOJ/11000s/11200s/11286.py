import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
