class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_diag_sq = 0
        max_area = 0

        for l, w in dimensions:
            diag_sq = l*l + w*w
            
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                max_area = l * w
            elif diag_sq == max_diag_sq:
                max_area = max(max_area, l * w)
                
        return max_area
