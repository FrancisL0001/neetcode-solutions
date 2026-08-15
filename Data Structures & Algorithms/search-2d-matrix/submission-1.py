class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if target <= matrix[row][-1] and target >= matrix[row][0]:
                l, r = 0, len(matrix[row]) - 1 
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
        return False   