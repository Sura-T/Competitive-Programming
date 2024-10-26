class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize variables
        start = 0
        end = 0
        
        # Iterate through the string
        for i in range(len(s)):
            # Check for palindromes with odd length
            len1 = self.expandFromCenter(s, i, i)
            
            # Check for palindromes with even length
            len2 = self.expandFromCenter(s, i, i + 1)
            
            # Find the length of the longest palindrome centered at the current character
            length = max(len1, len2)
            
            # Update the start and end indices if a longer palindrome is found
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        # Return the longest palindrome substring
        return s[start:end+1]
    
    def expandFromCenter(self, s: str, left: int, right: int) -> int:
        # Expand from the center to find the length of the palindrome substring
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return the length of the palindrome substring
        return right - left - 1