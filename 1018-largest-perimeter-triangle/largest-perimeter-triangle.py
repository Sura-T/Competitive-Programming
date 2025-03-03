class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = 2
        ans = 0
        while r < len(nums):
            if nums[l] + nums[r - 1] > nums[r]:
                ans = max(ans, nums[l] + nums[r - 1] + nums[r])

            l += 1
            r += 1

        return ans