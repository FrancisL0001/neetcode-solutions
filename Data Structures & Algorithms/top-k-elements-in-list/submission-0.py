class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            if num in my_map:
                my_map[num] += 1
            else:
                my_map[num] = 1

        sorted_values = sorted(my_map.items(), 
                                key = lambda item: item[1], 
                                reverse=True)
        
        return [item[0] for item in sorted_values[:k]]
        