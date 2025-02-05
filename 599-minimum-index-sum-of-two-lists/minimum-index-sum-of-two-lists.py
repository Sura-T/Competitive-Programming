class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = {}
        least_index = float('inf') 
        for word in list1:
            if word in list2:
                x = list1.index(word) + list2.index(word)
                res[word] = x
        min_value = min(res.values())
        return [key for key,value in res.items() if value == min_value]
                
            