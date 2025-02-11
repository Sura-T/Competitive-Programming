class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j < n and j != i and nums[j] < nums[i]:
                    cnt +=1
            res.append(cnt)

        return res
        

            



        