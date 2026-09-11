
# 36. Valid Sudoku

class Solution(object):
    def is_valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # rows check: verify only 1-9
        for row in board:
            mem_dict = {}
            for element in row:
                if element != ".":
                    if element not in mem_dict:
                        mem_dict[element] = 1
                    else:
                        mem_dict[element] += 1
                    if mem_dict[element] > 1:
                        return False

        # column check: verify only 1-9
        row_num = len(board)
        col_num = len(board[0])

        for i in range(0, row_num):
            mem_dict = {}
            for j in range(0, col_num):
                element = board[j][i]
                if element != ".":
                    if element not in mem_dict:
                        mem_dict[element] = 1
                    else:
                        mem_dict[element] += 1
                    if mem_dict[element] > 1:
                        return False

        # check sub-matrix 3x3: verify only 1-9
        sub_row_len = 3
        sub_col_len = 3

        row_offset = 0
        while row_offset < 9:

            col_offset = 0
            while col_offset < 9:
                mem_dict = {}
                for i in range(row_offset, sub_row_len + row_offset):
                    for j in range(col_offset, sub_col_len + col_offset):
                        element = board[i][j]
                        if element != ".":
                            if element not in mem_dict:
                                mem_dict[element] = 1
                            else:
                                mem_dict[element] += 1
                            if mem_dict[element] > 1:
                                return False
                col_offset += 3

            row_offset += 3

        return True

if __name__ == "__main__":

    s_board = \
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s1 = Solution()
    res = s1.is_valid_sudoku(s_board)
    print(res)