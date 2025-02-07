class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for path in paths:
            res = path.split(" ")
            directory = res[0]

            for file_info in res[1:]:
                filename,content = file_info.split("(")
                content = content[:-1]

                full_path = directory +  "/" + filename
                my_dict[content].append(full_path)

        return [duplicate for duplicate in my_dict.values() if len(duplicate) > 1]