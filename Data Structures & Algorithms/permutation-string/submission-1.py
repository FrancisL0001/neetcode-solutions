class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False 

        s1_arr, s2_arr = [0] * 26, [0] * 26

        for i in range(m):
            s1_arr[ord(s1[i]) - ord("a")] += 1
            s2_arr[ord(s2[i]) - ord("a")] += 1

        num_match = 0

        for i in range(26):
            num_match += 1 if s1_arr[i] == s2_arr[i] else 0

        l = 0

        for r in range(m, n):
            if num_match == 26:
                return True

            idx = ord(s2[l]) - ord("a")
            s2_arr[idx] -= 1
            if s1_arr[idx] == s2_arr[idx]:
                num_match += 1
            elif s1_arr[idx] == s2_arr[idx] + 1:
                num_match -= 1
            l += 1
            
            idx = ord(s2[r]) - ord("a")
            s2_arr[idx] += 1
            if s1_arr[idx] == s2_arr[idx]:
                num_match += 1
            elif s1_arr[idx] == s2_arr[idx] - 1:
                num_match -= 1

        return num_match == 26
                