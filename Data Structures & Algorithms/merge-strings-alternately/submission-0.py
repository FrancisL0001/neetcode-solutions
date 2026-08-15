class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1 = 0
        str2 = 0

        n = len(word1)
        m = len(word2)

        res = ""

        while str1 < n and str2 < m:
            res += word1[str1] + word2[str2]
            str1+=1
            str2+=1
        
        while str1 < n:
            res += word1[str1]
            str1+=1

        while str2 < m:
            res += word2[str2]
            str2 += 1

        return res
