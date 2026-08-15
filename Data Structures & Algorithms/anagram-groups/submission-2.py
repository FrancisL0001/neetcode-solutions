def isAnagram(s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seen1 = {}
        seen2 = {}

        for i in range(len(s)):
            if s[i] in seen1:
                seen1[s[i]] += 1
            else:
                seen1[s[i]] = 1

            if t[i] in seen2:
                seen2[t[i]] += 1
            else:
                seen2[t[i]] = 1 
        
        return seen1 == seen2


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = []

        for s in strs:
            if s in seen:
                continue
            an = []
            for t in strs:
                if isAnagram(s, t):
                    an.append(t)
            if not an in res:
                res.append(an)
        
        return res