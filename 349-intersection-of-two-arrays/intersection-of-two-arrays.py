class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for i in nums1 :
            hashmap[i] = True
        
        for i in nums2 :
            if i in hashmap and hashmap[i]:
                res.append(i)
                hashmap[i] = False
                
        return res