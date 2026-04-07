class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(r, c):
            #все связанные клетки '1' превращаются в '0'."""
            queue = deque([(r, c)])
            grid[r][c] = '0'  #помечается как посещённое
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        queue.append((nx, ny))
        
        #сканирование всей сетки
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        return count