class Solution:
    def printVertically(self, s: str) -> List[str]:
        list1 = s.split(" ")
        max_length = max(len(word) for word in list1)
        result = [""] * max_length

        for i in range(max_length):
            for word in list1:
                result[i] += word[i] if i < len(word) else " " 

        
        return [line.rstrip() for line in result]

        
            