class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum(ceil(p / mid) for p in piles)
        
            if hours > h:
                left = mid + 1  
            else:
                right = mid  
    
        return left 