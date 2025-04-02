class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_value = max(max_value, (nums[i] - nums[j]) * nums[k])

        return max_value