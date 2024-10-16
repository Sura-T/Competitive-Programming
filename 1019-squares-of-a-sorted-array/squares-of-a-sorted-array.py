class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        e = len(nums) - 1
        res = [0] * len(nums)
        idx = len(nums) - 1

        while idx > -1:
            if abs(nums[s]) > abs(nums[e]):
                res[idx] = nums[s] ** 2
                s += 1
            else:
                res[idx] = nums[e] ** 2
                e -= 1
            idx -=1
        return res
        