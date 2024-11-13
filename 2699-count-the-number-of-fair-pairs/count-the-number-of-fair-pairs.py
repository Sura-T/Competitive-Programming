class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  
        cnt = 0
        n = len(nums)
        
        for i in range(n - 1):
            left = self.findLeft(nums, i + 1, n - 1, lower - nums[i])
            right = self.findRight(nums, i + 1, n - 1, upper - nums[i])
            
            if left != -1 and right != -1:
                cnt += (right - left + 1)
        
        return cnt

    def findLeft(self, nums: List[int], start: int, end: int, target: int) -> int:
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start if start < len(nums) else -1

    def findRight(self, nums: List[int], start: int, end: int, target: int) -> int:
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return end if end >= 0 else -1
