class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(x):
            required_stores = 0
            for quantity in quantities:
                required_stores += (quantity + x - 1) // x
            return required_stores <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  
            else:
                left = mid + 1  
    
        return left