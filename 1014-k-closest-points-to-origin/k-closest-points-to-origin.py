class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            dist = x*x + y*y #квадрат расстояния без sqrt для скорости
            heapq.heappush(h, (-dist, x, y))  #отриц. для кучи
            if len(h) > k:
                heapq.heappop(h)  #удаление наибольш. расст.
        res = []
        for dist, x, y in h:
            res.append([x, y])
        
        return res