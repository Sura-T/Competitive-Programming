class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            cur = nums[i] - 1
            if nums[cur] != nums[i]:
                nums[cur], nums[i] = nums[i], nums[cur]

            else:
                i += 1
        res = []
        for i in range(n):
            if nums[i] - 1 != i:
                res.append(nums[i])
                res.append(i + 1)
      
        return res