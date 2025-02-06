class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product1 = defaultdict(int)
        for i in range(1,len(nums)):
            for j in range(i):
                    x = nums[i] * nums[j]
                    product1[x] += 1

        total_tuples = sum(count * (count - 1) // 2 for count in product1.values()) << 3

        return total_tuples