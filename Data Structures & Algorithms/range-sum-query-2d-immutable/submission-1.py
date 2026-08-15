class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''
        
            Here, we will sacrifice so initial preprocessing time in the initialization step. 
            Essentially, our inner matrix will store, on each position, the sum of the region from the beginning to that position:
            M[n,m] = sum(i, j = 0 -> n, m) [M[i,j]]

            This will help in making sumRegion() an O(1) later on

            M[i,j] = M[i,j] + M[i, j-1] + M[i-1, j] - M[i-1,j-1];
            
            And we set the top column and first row intially by iterating through the 0 indexed-terms
                 
        '''
        self.matrix = matrix

        for i in range(1, len(matrix[0])):
            self.matrix[0][i] = self.matrix[0][i] + self.matrix[0][i-1]
        
        for i in range(1, len(matrix)):
            self.matrix[i][0] = self.matrix[i][0] + self.matrix[i-1][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][j-1] + self.matrix[i-1][j] - self.matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        
        sum = M[r2,c2] - M[r1-1,c2] - M[r2,c1-1] + M[r1-1,c1-1]

        care should be taken when r1 or c1 = 0 to avoid undefined behaviors
        
        '''

        if row1 == col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        else: 
            return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)