from collections import deque

def solution(maps):
    answer = 0
    height, width = len(maps), len(maps[0])
    flag = False
    

    # 일반적인 bfs 로직. 
    def bfs(start, end):
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = [[False] * width for _ in range(height)]
        flag = False
        
        for i in range(height):
            for j in range(width):
                if maps[i][j] == start:
                    start_pt = [i,j]
                    flag = True
                    break
            if flag: break
        
        q = deque([start_pt])
        cnt = 0

        # 비용 cnt를 계산하기 위해서 한 단계에 움직일 수 있는 점들을 queue에 한 번에 모아 for loop로 해결. 그러나 시간 초과 야기.
        while q:
            cnt += 1
            #print(f"Level: {cnt}")
            for n in range(len(q)):
                i, j = q.popleft()
                visited[i][j] = True
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < height and 0 <= nj < width and maps[ni][nj] == end:
                        return cnt
                    elif 0 <= ni < height and 0 <= nj < width and maps[ni][nj] != 'X' and not visited[ni][nj]:
                        q.append([ni, nj])
                        #print(f"ni, nj: {ni}, {nj}")
        return -1
    
                        
    start_to_lev = bfs('S', 'L')
    lev_to_end = bfs('L', 'E')
    
    if start_to_lev < 0 or lev_to_end < 0:
        return -1
    else:
        return start_to_lev + lev_to_end
    
    return answer
