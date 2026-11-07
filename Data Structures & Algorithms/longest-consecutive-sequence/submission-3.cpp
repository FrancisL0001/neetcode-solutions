class Solution {
public:
    unordered_map<int, int> parents;

    int find(int num){ 
        if (parents[num] != num){ // path compression
            parents[num] = find(parents[num]);
        }
        return parents[num];
    }

    void sUnion(int n, int m){
        int parent_n = find(n);
        int parent_m = find(m);

        if (parent_n < parent_m){
            parents[parent_m] = parent_n;
        } else if (parent_n > parent_m){
            parents[parent_n] = parent_m;
        }
    }

    int longestConsecutive(vector<int>& nums) {
        parents.clear();
        for (int num : nums){
            parents[num] = num;
        }

        for (int num : nums){
            if (parents.contains(num - 1)){
                sUnion(num, num - 1);
            } else if (parents.contains(num + 1)){
                sUnion(num, num + 1);
            }
        }
        unordered_map<int, int> count; 
        for (const auto& [val, parent] : parents){
            count[find(val)]++;
        }
        int res = 0;
        for (const auto& [parent, freq] : count){
            res = max(res, freq);
        }

        return res;
    }
};
