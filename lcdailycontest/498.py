class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows, num_cols = len(matrix), len(matrix[0])
      
        diagonal_order = []
      
        for k in range(num_rows + num_cols - 1):
          
            temp = []
          
            row = 0 if k < num_cols else k - num_cols + 1
          
            col = k if k < num_cols else num_cols - 1
          
            while row < num_rows and col >= 0:
                temp.append(matrix[row][col])
                row += 1
                col -= 1
          
            if k % 2 == 0:
                temp = temp[::-1]
          
            diagonal_order.extend(temp)
      
        return diagonal_order
