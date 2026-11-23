class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<int> pq;
        unordered_map<int, int> window;

        for (int i = 0; i < k; i++){
            pq.push(nums[i]);
            window[nums[i]]++;;
        }

        vector<int> res;
        res.push_back(pq.top());
        int l = 0;
        for (int r = k; r < nums.size(); r++){
            window[nums[l]]--;
            l++;
            while (pq.size() > 0 && window[pq.top()] < 1){
                pq.pop();
            }
            pq.push(nums[r]);
            window[nums[r]]++;
            res.push_back(pq.top());
        }

        return res;
    }
};
