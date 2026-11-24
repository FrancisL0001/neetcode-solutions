class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // ceil(num)
        // get arrival time for a car, check if the previous fleet
        // arrives at or before the time this one arrives
        // if it does, remove that fleet as it joins the current one
        // else just add this car to the stack

        stack<float> arrivalTimes;
        vector<pair<int, int>> fleets;
        for (int i = 0; i < position.size(); i++){
            fleets.push_back(make_pair(position[i], speed[i]));
        }

        sort(fleets.begin(), fleets.end());

        for (int i = 0; i < fleets.size(); i++){
            float distance = target - fleets[i].first;
            float arrival = (distance / fleets[i].second);
            cout << arrival << "\n";

            while (arrivalTimes.size() > 0 && arrival >= arrivalTimes.top()){
                arrivalTimes.pop();
            }
            arrivalTimes.push(arrival);
        }

        return arrivalTimes.size();
    }
};
