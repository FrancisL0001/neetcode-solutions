class Solution {
public:
    int maxProfit(vector<int>& prices) {  
        int maxGain = 0;
        int minBuy = prices[0];
        
        for (int price : prices){
            maxGain = max(maxGain, price - minBuy);
            minBuy = min(minBuy, price);
        }

        return maxGain;
    }
};
