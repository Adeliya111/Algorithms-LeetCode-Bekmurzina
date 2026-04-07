from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #построение графа в виде списка смежности
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        #мин время от k до i
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for nei, weight in graph[node]:
                new_time = time + weight
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))
        
        max_time = max(dist[1:])  #игнорируем индекс 0
        return max_time if max_time != float('inf') else -1