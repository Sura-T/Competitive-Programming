class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        subarray_sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        subarray_sums[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            subarray_sums[i] = current_sum
        
        left = [0] * len(subarray_sums)
        right = [0] * len(subarray_sums)
        
        max_index = 0
        for i in range(len(subarray_sums)):
            if subarray_sums[i] > subarray_sums[max_index]:
                max_index = i
            left[i] = max_index
        
        max_index = len(subarray_sums) - 1
        for i in range(len(subarray_sums) - 1, -1, -1):
            if subarray_sums[i] >= subarray_sums[max_index]: 
                max_index = i
            right[i] = max_index
        
        max_sum = 0
        result = []
        for middle in range(k, len(subarray_sums) - k):
            left_index = left[middle - k]
            right_index = right[middle + k]
            total = subarray_sums[left_index] + subarray_sums[middle] + subarray_sums[right_index]
            if total > max_sum:
                max_sum = total
                result = [left_index, middle, right_index]
        
        return result
