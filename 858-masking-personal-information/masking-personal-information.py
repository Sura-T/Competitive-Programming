class Solution:
    def maskPII(self, s: str) -> str:
        s = s.lower()
        if '@' in s:
            index_at = s.index('@')
            
            masked_email = s[0] + "*****" + s[index_at-1:]
            return masked_email
        else:
            res = ''
            separation = ['+','-','(',')',' ']
            for i in range(len(s)):
                if s[i] not in separation:
                    res += s[i]
        
            if len(res) == 10:
                return 3*'*' + '-' + 3 * '*' + '-' + res[-4:]

            if len(res) == 11:
                return '+*' + '-' + 3*'*' + '-' + 3 * '*' + '-' + res[-4:]
            if len(res) == 12:
                return '+**' + '-' + 3*'*' + '-' + 3 * '*' + '-' + res[-4:]
            if len(res) == 13:
                return '+***' + '-' + 3*'*' + '-' + 3 * '*' + '-' + res[-4:]

            