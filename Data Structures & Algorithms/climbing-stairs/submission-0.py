class Solution:
    def climbStairs(self, n: int) -> int:
        memo_table = {
            1: 1, 
            2: 2
        }

        def dp(num : int) -> int:
            if num in memo_table:
                return memo_table[num]

            cur = dp(num - 1) + dp(num - 2)
            memo_table[num] = cur

            return cur

        return dp(n)
            