class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ps = 0
        res = []
        for num in nums:
            ps += num
            res.append(ps)
        if min(res) < 0:
            start_Value = 1 - min(res)
        else:
            start_Value = 1
        return start_Value

