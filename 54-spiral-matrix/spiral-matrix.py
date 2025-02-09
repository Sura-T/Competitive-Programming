class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row, col = len(matrix), len(matrix[0])
        
        top, bottom, left, right = 0, row - 1, 0, col - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1  # Move down to the next row
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # Move left to the next column
            
            if top <= bottom:
                # Traverse from right to left
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1  # Move up to the previous row
            
            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # Move right to the next column
        
        return res
