class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        #to find the middle number
        if num % 3 == 0:
            x = int(num/3)
        
            return [x-1, x, x + 1]
        return []