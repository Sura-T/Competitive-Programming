class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        name_height_pairs = list(zip(names, heights))

    
        sorted_pairs = sorted(name_height_pairs, key=lambda x: x[1], reverse=True)

    
        sorted_names = [name for name, _ in sorted_pairs]
        return sorted_names

        