class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min(len(s) for s in strs)

        if minLen == 0:
            return ""

        res = ""
        
        for i in range(minLen):
            cur = strs[0][i]
            for st in strs:
                if st[i] == cur:
                    continue
                else:
                    return res
            res += cur
        
        return res