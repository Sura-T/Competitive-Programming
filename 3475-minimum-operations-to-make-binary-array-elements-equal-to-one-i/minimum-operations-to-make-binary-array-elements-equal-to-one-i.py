class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i + 2 >= len(nums):
                    return -1

                nums[i + 1] ^= 1 
                nums[i + 2] ^= 1
                ans += 1
           

        return ans