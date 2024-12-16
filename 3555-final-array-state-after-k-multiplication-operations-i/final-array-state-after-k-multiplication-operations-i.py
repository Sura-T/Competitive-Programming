class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            x = min(nums)
            y = nums.index(x)
            nums[y] = x * multiplier
        return nums