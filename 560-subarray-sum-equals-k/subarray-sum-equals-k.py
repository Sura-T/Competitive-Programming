class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {0:1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num
            if prefix - k in my_dict:
                count += my_dict[prefix - k]
        
            my_dict[prefix] = my_dict.get(prefix,0) + 1

        return count
        
        