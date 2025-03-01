class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        max_row = 0
        
        for i, row in enumerate(mat):
            count_ones = row.count(1)
            if count_ones > max_ones:
                max_ones = count_ones
                max_row = i
        
        return [max_row, max_ones]