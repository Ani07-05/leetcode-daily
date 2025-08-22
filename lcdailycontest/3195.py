class Solution(object):
    def minimumArea(self, grid):
        min_row = float('inf')
        max_row = float('-inf')
        min_col = float('inf')
        max_col = float('-inf')
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if value == 1:
                    min_row = min(min_row, row_index)
                    max_row = max(max_row, row_index)
                    min_col = min(min_col, col_index)
                    max_col = max(max_col, col_index)
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width
