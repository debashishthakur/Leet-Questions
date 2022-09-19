class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp not in h:
                h[temp] = [word]
            else:
                h[temp].append(word)
        return list(h.values())
    
