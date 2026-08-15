class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}

        n = len(s)

        maxL = l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxL = max(maxL, window[s[r]]) 

            if r - l + 1 > maxL + k:
                window[s[l]] -= 1
                l += 1    

        return n - l

                
