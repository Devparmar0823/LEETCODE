class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        columns=len(matrix[0])
        first_col_zero=False
        for r in range(rows):
            if matrix[r][0]==0:
                first_col_zero=True
            for c in range(1,columns):
                if matrix[r][c]==0:
                    matrix[r][0]=0
                    matrix[0][c]=0
        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for c in range(columns):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0