from collections import deque
import sys 
input = sys.stdin.readline

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

# 지도의 크기
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])