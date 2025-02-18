class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        my_dict = {0:1}
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            remainder = curr_sum % k

            if remainder < 0:
                remainder += k

            count += my_dict.get(remainder,0)
            my_dict[remainder] = my_dict.get(remainder,0) + 1

        return count



             
