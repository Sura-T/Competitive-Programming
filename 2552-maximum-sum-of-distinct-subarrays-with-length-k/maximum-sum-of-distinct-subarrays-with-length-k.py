class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        current_sum = 0
        max_sum = 0
        seen = {}
        l = 0

        for r in range(n):
            current_sum += nums[r]
            seen[nums[r]] = seen.get(nums[r], 0) + 1

            if r - l + 1 > k:
                current_sum -= nums[l]
                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    del seen[nums[l]]
                l += 1

            if r - l + 1 == k and len(seen) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
