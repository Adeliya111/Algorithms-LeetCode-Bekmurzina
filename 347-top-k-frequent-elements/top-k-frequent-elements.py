class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums) #частота каждого числа
        
        h = []
        for num, freq in c.items():
            heapq.heappush(h, (freq, num))  #частота и число
            if len(h) > k:
                heapq.heappop(h)  #удаление элемента с наименьшей частотой
        
        return [num for freq, num in h]
        