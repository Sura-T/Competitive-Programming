class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = [(heights[i], names[i]) for i in range(len(names))]
        
        for i in range(1, len(res)):
            height = res[i]
            j = i - 1
            while j >= 0 and res[j][0] < height[0]: 
                res[j + 1] = res[j]
                j -= 1
            res[j + 1] = height
        
        return [name[1] for name in res]
