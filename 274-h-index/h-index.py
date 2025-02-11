class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True) 
        n = len(citations)
        h_index = 0
        for index,citation in enumerate(citations):
            if citation >= index + 1:  
                h_index = index + 1
            else:
                break

        return h_index
        