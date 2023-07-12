#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        rs = [1] * len(heights) 
        can_see = []
        for i in range(len(heights) - 1, -1, -1):
            count = 0
            while len(can_see) != 0 and can_see[-1] < heights[i]:
                can_see.pop()
                count += 1
            if len(can_see) != 0:
                rs[i] += count
            else:
                rs[i] = count
            can_see.append(heights[i])
        return rs
# @lc code=end

