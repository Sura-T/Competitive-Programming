class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        my_dict = {'row1':'qwertyuiop', 'row2':'asdfghjkl', "row3":'zxcvbnm'}
        res = []
        for word in words:
            word_lower = word.lower()
            flag = True
            if word_lower[0] in my_dict['row1']:
                for i in range(len(word)):
                    if word_lower[i] not in my_dict['row1']:
                        flag = False
                        break

            if word_lower[0] in my_dict['row2']:
                flag = True
                for i in range(len(word)):
                    if word_lower[i] not in my_dict['row2']:
                        flag = False
                        break
                
            if word[0] in my_dict['row3']:
                flag = True
                for i in range(len(word)):
                    if word_lower[i] not in my_dict['row3']:
                        flag = False
                        break
            if flag:
                res.append(word)

            
        return res


    