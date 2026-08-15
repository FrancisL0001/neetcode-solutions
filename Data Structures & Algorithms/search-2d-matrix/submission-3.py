class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if target <= matrix[middle][-1] and target >= matrix[middle][0]:
                l, r = 0, len(matrix[middle]) - 1 
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[middle][mid] == target:
                        return True
                    elif matrix[middle][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            elif target > matrix[middle][-1]:
                left = middle + 1
            else:
                right = middle - 1
        return False   