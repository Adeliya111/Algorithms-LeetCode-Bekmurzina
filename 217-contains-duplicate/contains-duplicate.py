class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)) :
            a = nums[i]
            if a in hashmap :
                return True
            hashmap[nums[i]] = i
        return False