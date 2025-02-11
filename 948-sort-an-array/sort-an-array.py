class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        min_val = abs(min(nums))

        count = [0] * (max_val + min_val + 1)

        for num in nums:
            count[num + min_val] += 1

        result = []
        for index,value in enumerate(count):
            if value > 0:
                result.extend([index - min_val] * value)

        return result