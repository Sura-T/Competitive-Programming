class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict = {}
        res = []
        result = []
        for i in range(len(names)):
            my_dict[heights[i]] = names[i]
            
        for key in my_dict:
            res.append(key)
        res.sort(reverse=True)

        for i in res:
            result.append(my_dict[i])

        return result