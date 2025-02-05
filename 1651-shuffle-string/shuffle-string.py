class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [i for i in s]
        for i in range(len(res)):
            res[indices[i]] = s[i]

        return "".join(res)