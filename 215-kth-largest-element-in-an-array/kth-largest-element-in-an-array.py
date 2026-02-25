class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h) #превращение переменной в мин. кучу
        for i in nums[k:]:
            if i > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, i)
        return h[0]