class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        m, n = len(image), len(image[0])
        queue = deque([(sr, sc)])
        image[sr][sc] = newColor
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                #проверка границ сетки и совпадения с исходным цветом
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == oldColor:
                    image[nr][nc] = newColor  #замена цвета перед добавлением в очередь
                    queue.append((nr, nc))    #добавление соседа для дальнейшего обхода
        return image