class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()){
            return "";
        } 

        unordered_map<char, int> mp;
        vector<int> window(52, 0);
        int numMatches = 0;
        
        for (int i = 0; i < t.length(); i++){
            mp[t[i]]++;
            int idx = s[i] - 'a' >= 0 ? s[i] - 'a' : (s[i] - 'A') + 26;
            window[idx]++;
        }

        int count = 0;
        for (const auto& [c, val] : mp){
            int idx = c - 'a' >= 0 ? c - 'a' : (c - 'A') + 26;
            if (window[idx] >= val){
                numMatches++;
            }
            count++;
        } 
        cout << numMatches << " " << count <<"\n";
        bool found = false;
        int l_idx = 0, r_idx = s.length();
        int l = 0, r = t.length() - 1;

        while (r < s.length()){
            if (numMatches == count){
                cout << "found" << "\n";
                found = true;
                int idx = s[l] - 'a' >= 0 ? s[l] - 'a' : (s[l] - 'A') + 26;
                while ((not mp.contains(s[l])) || mp[s[l]] < window[idx]){
                    window[idx]--;
                    l++;
                    idx = s[l] - 'a' >= 0 ? s[l] - 'a' : (s[l] - 'A') + 26;
                }
                
                if (r_idx - l_idx > r - l + 1){
                    r_idx = r + 1;
                    l_idx = l;
                }
                window[idx]--;
                l++;
                numMatches--;
            }

            r++;
            if (r >= s.length()){
                break;
            }
            int idx = s[r] - 'a' >= 0 ? s[r] - 'a' : (s[r] - 'A') + 26;
            window[idx]++;
            if (mp.contains(s[r]) && mp[s[r]] == window[idx]){
                numMatches++;
            } 
        }

        if(found == true){
            string res = "";
            for (int j = l_idx; j < r_idx; j++){
                res += s[j];
            }
            return res;
        }
        return "";
    }
};
