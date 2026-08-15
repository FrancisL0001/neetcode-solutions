class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        n = len(s)

        cur_str = ""

        for c in s:
            cur_str += c
            if len(cur_str) == len(set(cur_str)):
                maxL = max(maxL, len(cur_str))
            else:
                while len(cur_str) != len(set(cur_str)):
                    cur_str = cur_str[1:]

        return maxL