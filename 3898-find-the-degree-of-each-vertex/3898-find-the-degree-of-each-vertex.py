class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        output=[0]*n
        for i in range(n):
            for j in range(n):
                if matrix[i][j]==1:
                    output[i]+=1
        return output