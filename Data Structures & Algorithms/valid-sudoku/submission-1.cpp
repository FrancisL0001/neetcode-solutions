class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<string, unordered_set<char>> squares;

        for (int i = 0; i < board.size(); i++){
            for (int j = 0; j < board.size(); j++){
                string sq_key = to_string(floor(i/3)) + ',' + to_string(floor(j/3));
                if (board[i][j] == '.'){
                    continue;
                } else if (rows[i].contains(board[i][j]) ||
                    cols[j].contains(board[i][j]) ||
                    squares[sq_key].contains(board[i][j])
                ){
                    return false;
                } else {
                    rows[i].insert(board[i][j]);
                    cols[j].insert(board[i][j]);
                    squares[sq_key].insert(board[i][j]);
                }
            }
        }

        return true;
    }
};
