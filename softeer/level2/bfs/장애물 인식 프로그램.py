import sys
from collections import deque

# Taking Inputs
n = int(sys.stdin.readline())
graph = []
for i in range(n):
    tmp = [int(c)  for c in sys.stdin.readline() if c != '\n']
    graph.append(tmp)
answer = []

# Define BFS Function
def bfs(i, j):
    directions= [[1,0], [-1,0], [0,1], [0,-1]]
    q = deque([[i,j]])  # 초기화 시 리스트를 담으려면 [[]] 주의
    graph[i][j] = 0
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            di += i
            dj += j
            if di>=0 and di<n and dj>=0 and dj<n:
                if graph[di][dj] == 1:
                    graph[di][dj] = 0
                    q.append([di, dj])
                    cnt += 1
    return cnt

# Traverse Graph Using BFS
for i, row in enumerate(graph):
    for j, digit in enumerate(row):
        if digit == 1:
            answer.append(bfs(i, j))

# Print Out Answers
answer.sort()
print(len(answer))
for i in answer:
    print(i)

