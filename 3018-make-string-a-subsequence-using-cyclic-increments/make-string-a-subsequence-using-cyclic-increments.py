class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0

        while j < len(str2):
            if i >= len(str1): 
                return False

            if str1[i] == str2[j]:  
                i += 1
                j += 1
            else:
                required_increment = (ord(str2[j]) - ord(str1[i]) + 26) % 26
                if required_increment == 1:  
                    i += 1 
                    j += 1  
                else:
                    i += 1  

        return True
