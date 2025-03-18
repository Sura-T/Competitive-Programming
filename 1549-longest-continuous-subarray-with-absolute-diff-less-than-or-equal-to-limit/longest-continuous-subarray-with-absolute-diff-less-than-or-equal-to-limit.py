class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl = SortedList()
        max_len = 0
        l = 0

        for r, val in enumerate(nums):
            sl.add(val)

            while sl[-1] - sl[0] > limit:
                sl.remove(nums[l])

                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len