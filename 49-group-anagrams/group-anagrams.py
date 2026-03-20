class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs :
            cnt = [0] * 26 #английские буквы
            for ch in word :
                cnt[ord(ch) - ord('a')] += 1 #ASCII 
            
            key = tuple(cnt)
            hashmap[key].append(word)
            
        return list(hashmap.values())