class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_columns = defaultdict(set)
        seen_squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if ((board[i][j] in seen_rows[i]) or 
                    (board[i][j] in seen_columns[j]) or
                    (board[i][j] in seen_squares[(i // 3, j // 3)])):
                    return False
                
                seen_rows[i].add(board[i][j])
                seen_columns[j].add(board[i][j])
                seen_squares[(i // 3, j // 3)].add(board[i][j])
        return True

    
        
        