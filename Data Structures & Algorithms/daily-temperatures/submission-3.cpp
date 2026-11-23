class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<vector<int>> temps;
        vector<int> res(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); i++){
            vector<int> current = {i, temperatures[i]};
            while (temps.size() > 0 && temperatures[i] > temps.top()[1]){
                res[temps.top()[0]] = i - temps.top()[0];
                temps.pop();
            }
            temps.push(current); 
        }

        return res;
    }
};
