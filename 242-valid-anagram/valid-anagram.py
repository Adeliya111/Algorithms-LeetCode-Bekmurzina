class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t) :
            return False
        for ch in s :
            hashmap[ch] = hashmap.get(ch, 0) + 1
        
        for ch in t :
            if ch not in hashmap :
                return False
            hashmap[ch] -= 1
            if hashmap[ch] < 0 :
                return False

        return True