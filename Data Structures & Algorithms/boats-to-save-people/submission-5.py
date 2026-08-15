class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        res = 0

        people.sort()

        l, r = 0, n - 1

        while l < r: 
            curSum = people[l] + people[r]

            if curSum <= limit:
                r -= 1
                l += 1
            else:
                r -= 1

            res += 1
        
        if l == r:
            res += 1
        
        return res