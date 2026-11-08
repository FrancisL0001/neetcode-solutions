class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2){
            return 0;
        }
        priority_queue<int> pq;
        int maxGain = 0;
        for (int price : prices){
            pq.push(-1 * price);
            maxGain = max(maxGain, price + pq.top());
        }
        return maxGain;
    }
};
