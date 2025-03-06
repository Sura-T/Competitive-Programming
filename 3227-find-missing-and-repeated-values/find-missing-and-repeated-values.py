class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hash_map = {}
        res = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in hash_map:
                    hash_map[grid[i][j]] = 1
                else:
                    hash_map[grid[i][j]] += 1
                    res.append(grid[i][j])
        for i in range(1,(n**2) + 1):
            if i not in hash_map:
                res.append(i)
        
        return res

        

