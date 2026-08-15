class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = maxL = res = 0
        count = {} 
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            res += 1
            maxL = max(maxL, count[s[r]])

            if res - maxL > k:
                count[s[l]] -= 1
                res -= 1
                l += 1

        return res

                
