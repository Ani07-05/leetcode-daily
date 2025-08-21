class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total_submatrices = 0


        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            for j in range(n):
                min_height = heights[j]
                for k in range(j, -1, -1):
                    min_height = min(min_height, heights[k])
                    if min_height == 0:
                        break
                    total_submatrices += min_height
                    
        return total_submatrices
