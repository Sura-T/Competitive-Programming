class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block_comment = False
        new_line = []

        for line in source:
            i = 0
            if not in_block_comment:
                new_line = []
            
            while i < len(line):
                if not in_block_comment and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block_comment = True
                    i += 1 
                elif in_block_comment and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block_comment = False
                    i += 1
                elif not in_block_comment and i + 1 < len(line) and line[i:i+2] == "//":
                    break
                elif not in_block_comment:
                    new_line.append(line[i])
                i += 1

            if new_line and not in_block_comment:
                result.append("".join(new_line))
        
        return result
