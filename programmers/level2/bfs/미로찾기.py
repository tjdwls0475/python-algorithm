from collections import deque

def solution(maps):
    height, width = len(maps), len(maps[0])
    flag = False

    # 더욱 효율적인 로직의 bfs 함수. visited array에 단순한 boolean이 아닌 cost를 기록하도록 한다.
    def bfs(start, end):
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = [[-1] * width for _ in range(height)]
        flag = False
        
        for i in range(height):
            for j in range(width):
                if maps[i][j] == start:
                    si, sj = i, j
                    flag = True
                    break
            if flag: break
        
        q = deque([[si, sj]])
        visited[si][sj] = 0

        # 굳이 쌓인 queue들을 for loop로 묶어서 돌리지 않더라도 visited list를 통해서 cost 카운팅이 가능하다.
        while q:
            i, j = q.popleft()
            #print(i, j)
            if maps[i][j] == end:
                return visited[i][j]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                    
                if 0 <= ni < height and 0 <= nj < width and maps[ni][nj] != 'X' and visited[ni][nj] == -1:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
        return -1
                        
    start_to_lev = bfs('S', 'L')
    lev_to_end = bfs('L', 'E')
    
    if start_to_lev == -1 or lev_to_end == -1:
        return -1
    else:
        return start_to_lev + lev_to_end
