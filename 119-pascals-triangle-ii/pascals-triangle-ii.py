class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        f = [[1]]
        for i in range(numRows-1):
            g = [1] + [a+b for a,b in pairwise(f[-1])] + [1]
            f.append(g)
            
        return f[rowIndex]