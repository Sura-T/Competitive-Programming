class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        prefix = [0] * (n + 1)
        for start,end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
        
        for i in range(1,n + 1):
            prefix[i] += prefix[i - 1]
        
        prefix = [prefix[i] for i in range(n)]
        prefix.sort()
        nums.sort()
        
        val = 0
        for i in range(n):
            val += (nums[i] * prefix[i])

        return val % mod