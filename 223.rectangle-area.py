#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        width_a = ay2 - ay1
        length_a = ax2 - ax1
        width_b = by2 - by1
        length_b = bx2 - bx1
        total = width_a*length_a + width_b*length_b
        
        overlap_x = min(ax2,bx2) - max(ax1,bx1)
        overlap_y = min(ay2,by2) - max(ay1,by1)

        if overlap_x > 0 and overlap_y > 0:
            return total - overlap_x*overlap_y
        else: 
            return total
# @lc code=end

