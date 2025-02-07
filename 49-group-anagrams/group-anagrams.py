class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        res = []
        for word in strs:
            sorted_word = tuple(sorted(word))
            my_dict[sorted_word].append(word)
            
        return list(my_dict.values())
