# 1. 고정된 사이즈라면 list보다는 tuple을 이용하기
# 2. if 문에서 and 조건이 병령로 나열된다면 순서대로 돌기 때문에 index 초과 여부를 먼저 체킹하도록만 짜면 되는 부분
# 3. 가독성을 위해 di, dj를 재활용하기보기보다는 ni, nj를 새로 선언하여 사용하기
# 4. 변수명
import sys
from collections import deque

# Taking Inputs
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    row = [int(c)  for c in sys.stdin.readline() if c != '\n']
    graph.append(row)
answer = []

# Define BFS Function
def bfs(i, j):
    directions= [[1,0], [-1,0], [0,1], [0,-1]]
    q = deque([(i,j)])
    graph[i][j] = 0
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if ni>=0 and ni<n and nj>=0 and nj<n and graph[ni][nj] == 1:
                graph[ni][nj] = 0
                q.append((ni, nj))
                cnt += 1
    return cnt

# Traverse Graph Using BFS
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

# Print Out Answers
answer.sort()
print(len(answer))
for size in answer:
    print(size)

