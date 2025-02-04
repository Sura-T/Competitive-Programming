class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index,num1 in enumerate(nums):
            num2 = target - num1
            if num2 in my_dict:
                return [my_dict[num2],index]
            else:
                my_dict[num1] = index
        return []

        
            