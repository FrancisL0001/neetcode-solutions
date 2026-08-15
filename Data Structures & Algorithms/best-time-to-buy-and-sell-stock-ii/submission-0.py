class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 0
        bought = False

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                if bought:
                    continue
                else:
                    buy += prices[i]
                    bought = True
            elif bought:
                sell += prices[i]
                bought = False
            else:
                continue

        if bought:
            sell += prices[-1]
        
        return sell - buy
