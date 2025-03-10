class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        num3 = float('-inf')
        stack = []

        for number in reversed(nums):
            if number < num3:
                return True
            
            while stack and stack[-1] < number:
                num3 = stack.pop()
            
            stack.append(number)

        return False
            
