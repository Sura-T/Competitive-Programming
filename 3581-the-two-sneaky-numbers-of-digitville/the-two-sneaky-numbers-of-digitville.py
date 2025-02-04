class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        my_dict = Counter(nums)
        res = []
        for i in my_dict:
            if my_dict[i] == 2:
                res.append(i)

        return res
                