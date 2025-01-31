class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        word = ''
        while i < len(command):
            if command[i] == "G":
                word += "G"
                i += 1
            elif command[i:i+2] == "()":
                word += 'o'
                i += 2
            elif command[i:i+4] == "(al)":
                word += "al"
                i += 4

        return word