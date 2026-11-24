class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // first look for matching row, O(log(m))
        // then inside matching row look for matching column, O(log(n))

        int l = 0, r = matrix.size() - 1;
        int row = (l + r) / 2;

        while (l <= r){
            if (matrix[row][0] <= target && matrix[row].back() >= target){
                break;
            } else if (matrix[row][0] > target){
                r = row - 1;
            } else {
                l = row + 1;
            }
            row = (l + r) / 2;
        }

        l = 0;
        r = matrix[0].size() - 1;
        while (l <= r){
            int mid = (l + r) / 2;
            if (matrix[row][mid] == target){
                return true;
            } else if (matrix[row][mid] > target){
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return false;
    }
};
