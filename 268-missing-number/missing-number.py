class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = [i for i in range(0, len(nums) + 1) if i not in nums]

        return result[0]

