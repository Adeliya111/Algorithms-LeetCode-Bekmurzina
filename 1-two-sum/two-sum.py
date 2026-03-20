class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)) :
            a = target - nums[i]
            if a in hashmap :
                return [hashmap[a], i]
            hashmap[nums[i]] = i
        return []