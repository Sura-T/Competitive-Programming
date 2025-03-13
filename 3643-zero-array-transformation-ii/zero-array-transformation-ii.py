class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(k):
            diff_array = [0] * (len(nums) + 1)
            for left, right, val in queries[:k]:
                diff_array[left] += val
                diff_array[right + 1] -= val

            cur_sum = 0
            for original, change in zip(nums, diff_array):
                cur_sum += change
                if original > cur_sum:
                    return False
            return True

        num_query = len(queries)
        l = bisect_left(range(num_query + 1), True, key = check)

        return -1 if l > num_query else l
