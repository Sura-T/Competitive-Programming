class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m = len(mat)
        n = len(mat[0])

        diagonals = {}
        res = []

        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])
        
        for key in sorted(diagonals):
            if key % 2 == 0:
                res.extend(reversed(diagonals[key]))
            else:
                res.extend(diagonals[key])

        return res
