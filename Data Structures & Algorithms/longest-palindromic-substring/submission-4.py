class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            j = 1
            cur1 = s[i]
            while 0 <= i - j and i + j < len(s) and s[i - j] == s[i + j]:
                cur1 = s[i - j] + cur1 + s[i + j]
                j += 1

            l, r = i - 1, i
            cur2 = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur2 = s[l] + cur2 + s[r]
                l -= 1
                r += 1    

            cur = cur1 if len(cur1) > len(cur2) else cur2

            if len(longest) < len(cur):
                    longest = cur

        return longest