class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> temps;
        vector<int> res(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); i++){
            while (temps.size() > 0 && temperatures[i] > temps.top().second){
                res[temps.top().first] = i - temps.top().first;
                temps.pop();
            }
            temps.push(make_pair(i, temperatures[i])); 
        }

        return res;
    }
};
