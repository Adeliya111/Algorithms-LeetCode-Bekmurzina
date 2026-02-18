class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        tl = 0
        r = len(nums) - 1

        while tl <= r:
            mid = (tl + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                tl = mid + 1

            else:
                r = mid - 1

        return tl 