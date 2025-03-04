class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # finding the rows max
        row_max = []

        for i in range(row):
            row_max.append(max(grid[i]))

        print("row", row_max)

        # finding the cols max
        col_max = []

        for i in range(col):
            arr = []
            for j in range(row):
                arr.append(grid[j][i])

            col_max.append(max(arr))

        print("cols", col_max)


        # totla
        total = 0

        for i in range(row):
            for j in range(col):
                max_hight_row = row_max[i]
                max_hight_col = col_max[j]

                zmin = min(max_hight_row, max_hight_col)
                total += zmin - grid[i][j]

        return total 