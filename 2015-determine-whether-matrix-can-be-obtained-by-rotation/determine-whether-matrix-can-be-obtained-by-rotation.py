class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat) 
        rotation = n - 1
        if mat == target:
            return True
        for _ in range(3):
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

            for row in mat:
                row.reverse()

            if mat == target:
                return True
        
        return False

