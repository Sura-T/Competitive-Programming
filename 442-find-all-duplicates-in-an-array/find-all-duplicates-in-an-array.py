class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        i = 0
        while i < n:
            curr = nums[i] - 1
            if nums[curr] != nums[i]:
                nums[curr], nums[i] = nums[i], nums[curr]

            else:

                i += 1

        for i in range(n):
            if nums[i] - 1 == i:
                continue
            else:
                arr.append(nums[i])
                
        return arr
