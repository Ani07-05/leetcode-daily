import math

class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        min_total_area = float('inf')

        def get_min_area(r1, c1, r2, c2):
            min_r, max_r = float('inf'), float('-inf')
            min_c, max_c = float('inf'), float('-inf')
            found_one = False
            
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        found_one = True
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
            
            if not found_one:
                return float('inf')
            
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        for i in range(m - 2):
            for j in range(i + 1, m - 1):
                area1 = get_min_area(0, 0, i, n - 1)
                area2 = get_min_area(i + 1, 0, j, n - 1)
                area3 = get_min_area(j + 1, 0, m - 1, n - 1)
                min_total_area = min(min_total_area, area1 + area2 + area3)


        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                area1 = get_min_area(0, 0, m - 1, i)
                area2 = get_min_area(0, i + 1, m - 1, j)
                area3 = get_min_area(0, j + 1, m - 1, n - 1)
                min_total_area = min(min_total_area, area1 + area2 + area3)


        for i in range(m - 1):
            for j in range(n - 1):
                a1 = get_min_area(0, 0, i, j)
                a2 = get_min_area(0, j + 1, i, n - 1)
                a3 = get_min_area(i + 1, 0, m - 1, n - 1)
                min_total_area = min(min_total_area, a1 + a2 + a3)
                
                a1 = get_min_area(0, 0, i, n - 1)
                a2 = get_min_area(i + 1, 0, m - 1, j)
                a3 = get_min_area(i + 1, j + 1, m - 1, n - 1)
                min_total_area = min(min_total_area, a1 + a2 + a3)

        for j in range(n - 1):
            for i in range(m - 1):
                a1 = get_min_area(0, 0, i, j)
                a2 = get_min_area(i + 1, 0, m - 1, j)
                a3 = get_min_area(0, j + 1, m - 1, n - 1)
                min_total_area = min(min_total_area, a1 + a2 + a3)
                
                a1 = get_min_area(0, 0, m - 1, j)
                a2 = get_min_area(0, j + 1, i, n - 1)
                a3 = get_min_area(i + 1, j + 1, m - 1, n - 1)
                min_total_area = min(min_total_area, a1 + a2 + a3)

        return min_total_area
    

#     You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

# Return the minimum possible sum of the area of these rectangles.

# Note that the rectangles are allowed to touch.

 
