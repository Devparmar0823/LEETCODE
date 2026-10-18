class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])
        
        left_col, right_col = 0, n - 1
        
        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2
            
            # Find the global maximum in the current column (mid_col)
            # This automatically satisfies the row-wise peak condition.
            max_row = 0
            for r in range(1, m):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r
            
            # Check neighbors to the left and right
            left_is_greater = mid_col > 0 and mat[max_row][mid_col - 1] > mat[max_row][mid_col]
            right_is_greater = mid_col < n - 1 and mat[max_row][mid_col + 1] > mat[max_row][mid_col]
            
            if not left_is_greater and not right_is_greater:
                # Found a 2D peak
                return [max_row, mid_col]
            elif right_is_greater:
                # Move to the right half
                left_col = mid_col + 1
            else:
                # Move to the left half
                right_col = mid_col - 1
                
        return []
