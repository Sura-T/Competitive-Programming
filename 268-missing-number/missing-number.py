class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) * (len(nums)+1) // 2
        return res - sum(nums)

