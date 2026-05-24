class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row increasing order
        # column increasing order

        l, r = 0, len(matrix) - 1

        m = -1
        while l <= r:
            m = l + (r - l) // 2
            
            if target < matrix[m][0]:
                r = m - 1
            
            elif target > matrix[m][-1]:
                l = m + 1
            
            else:
                break

        if not l <= r:
            return False
        
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            m2 = l + (r - l) // 2
            if matrix[m][m2] < target:
                l = m2 + 1
                    
            elif matrix[m][m2] > target:
                r = m2 - 1
                    
            else:
                return True
        return False 