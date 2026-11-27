class TimeMap {

private:
    unordered_map<string, vector<pair<int, string>>> kvstore;

public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        kvstore[key].push_back(make_pair(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        // vector<pair<int, string>> ls(kvstore[key]);
        int n = kvstore[key].size();
        int l = 0, r = n - 1;

        if (n < 1){
            return "";
        }

        string res = "";
        while (l <= r){
            int mid = (l + r) / 2;
            if (kvstore[key][mid].first <= timestamp){
                res = kvstore[key][mid].second;
                l = mid + 1;
            } else {
                r = mid - 1;
            } 
        }

        return res;

    }
};
