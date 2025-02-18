class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict = defaultdict(int)
        my_dict[0] = 1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            count += my_dict[curr_sum - goal]
            my_dict[curr_sum] += 1

        return count