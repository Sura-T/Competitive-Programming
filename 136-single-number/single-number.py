class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        for num, count in counts.items():
            if count == 1:
                return num
            

        