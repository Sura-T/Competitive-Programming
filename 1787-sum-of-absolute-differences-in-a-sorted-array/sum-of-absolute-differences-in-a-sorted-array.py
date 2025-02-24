class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []
        total_sum = sum(nums)
        prefix_sum = 0
        for i,value in enumerate(nums):
            current_sum = value * i - prefix_sum + total_sum - prefix_sum - value * (len(nums) - i)
          
            res.append(current_sum)
            prefix_sum += value
      
        return res

            