class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_val = 0
        max_val = 0
        ans = 0

        for num in nums:
            min_val = min(min_val,0) + num
            max_val = max(max_val, 0) + num

            ans = max(ans, max_val, abs(min_val))

        return ans