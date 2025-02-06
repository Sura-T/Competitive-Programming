class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] != nums[i+1]:
                i += 1
            elif i < len(nums)-1 and nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
                i += 1
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
               nums[k] = nums[i]
               k+=1
        for j in range(k,len(nums)):
            nums[j] = 0

        return nums