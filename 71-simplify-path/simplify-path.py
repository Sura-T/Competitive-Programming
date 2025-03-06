class Solution:
    def simplifyPath(self, path: str) -> str:
        newPath = path.split('/')
        stack = []

        for i in range(len(newPath)):
            if newPath[i] == '':
                continue
            elif newPath[i] == '.':
                continue
            elif newPath[i] == '..':
                if stack:
                    stack.pop()
                
            else:
                stack.append(newPath[i])
        print(stack)    
                
        
        
        return '/' + '/'.join(stack)
      


