class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones] #перевод в макс. кучу
        heapq.heapify(h)
        
        while len(h) > 1:
            #два самых тяжелых камня
            y = -heapq.heappop(h)  #самый тяжелый
            x = -heapq.heappop(h)  #второй по тяжести
            
            if x != y:
                heapq.heappush(h, -(y - x))  #остаток
        
        return -h[0] if h else 0 #возвр. 0 или последний камень
        