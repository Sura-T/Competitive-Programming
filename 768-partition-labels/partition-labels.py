class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {c:i for i,c in enumerate(s)}
        res = []
        max_last = partition_start = 0

        for index,character in enumerate(s):
            max_last = max(max_last,dic[character])

            if max_last == index:
                res.append(index - partition_start + 1)

                partition_start = index + 1

        return res
