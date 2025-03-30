class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_pos = -1 
        max_pos = -1  
        invalid_pos = -1  
        count = 0
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                invalid_pos = i  
            if num == minK:
                min_pos = i  
            if num == maxK:
                max_pos = i  
            
            count += max(0, min(min_pos, max_pos) - invalid_pos)
        
        return count
