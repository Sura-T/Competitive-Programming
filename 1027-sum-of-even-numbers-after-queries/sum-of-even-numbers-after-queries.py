class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        res = []

        for val,index in queries:
            old_val = nums[index]

            if old_val % 2 == 0:
                even_sum -= old_val

            nums[index] += val
            new_value = nums[index]

            if new_value % 2 == 0:
                even_sum += new_value
            
            res.append(even_sum)
        

        return res
