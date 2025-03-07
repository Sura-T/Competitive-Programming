class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = []
        curr = 0

        for num in nums:
            curr += num
            left_sum.append(curr - num)

        for i in range(1,n):
            nums[i] += nums[i - 1]
            
        for i in range(len(nums)):
            if left_sum[i] == nums[n-1] - nums[i]:
                return i
            
        return -1