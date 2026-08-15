class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] 
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)

            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = i - idx
                
                stack.append(i)
        
        return res

        

