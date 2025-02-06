class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ze_row=set()
        ze_col=set()
        row=len(matrix)
        col=len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    ze_row.add(i)
                    ze_col.add(j)
        for i in ze_row:
            for j in range(col):
                matrix[i][j]=0
        for j in ze_col:
            for i in range(row):
                matrix[i][j]=0


        return matrix