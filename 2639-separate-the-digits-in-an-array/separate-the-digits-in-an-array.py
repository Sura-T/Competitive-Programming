class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums = [str(num) for num in nums]
        nums = "".join(nums)
        nums = [int(num) for num in nums]
        
        return nums