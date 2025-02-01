class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            calculated_index = (i + nums[i] + n) % n
            result.append(nums[calculated_index])
        
        return result
