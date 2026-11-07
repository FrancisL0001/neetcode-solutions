class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maxV = 0;

        int l = 0, r = heights.size() - 1;

        while (l < r){
            int h = min(heights[l], heights[r]);
            int w = r - l;
            int curV = h * w;

            if (heights[r] > heights[l]){
                l++;
            } else {
                r--;
            }
            maxV = max(maxV, curV);
        }

        return maxV;
    }
};
