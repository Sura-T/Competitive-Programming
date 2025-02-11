class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        sub_boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell_value = board[i][j]
                if cell_value == '.':
                    continue

                num = int(cell_value) - 1
                box_index = (i //3 ) * 3 + j // 3

                if row[i][num] or cols[j][num] or sub_boxes[box_index][num]:
                    return False

                row[i][num] = True
                cols[j][num] = True
                sub_boxes[box_index][num] = True

        return True


