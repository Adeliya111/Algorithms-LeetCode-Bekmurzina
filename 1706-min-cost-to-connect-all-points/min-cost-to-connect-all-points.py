class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        
        minDist = [float('inf')] * n #массив мин расстояний от текущей до каждой вершины
        visited = [False] * n
        
        minDist[0] = 0
        total_cost = 0
        
        for _ in range(n): #непосещенная вершина с мин minDist
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i
            
            visited[u] = True #добавление вершины u в MST
            total_cost += minDist[u]
            
            for v in range(n): #обновление minDist для всех соседей
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < minDist[v]:
                        minDist[v] = dist
        
        return total_cost