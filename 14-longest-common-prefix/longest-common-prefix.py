class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix