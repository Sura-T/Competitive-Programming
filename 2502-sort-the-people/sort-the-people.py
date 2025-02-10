class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #counting sorting method
        height = defaultdict(list)
        
        max_height = max(heights)
        
        for i in range(len(names)):
            height[heights[i]].append(names[i])
        
        result = []
        for h in range(max_height, -1, -1):  
            if h in height:
                result.extend(height[h])  
        
        return result
