#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for circle in queries:
            count = 0
            for point in points:
                distance = math.sqrt((point[0] - circle[0])**2 + (point[1] - circle[1])**2)
                if distance <= circle[2]:
                    count += 1
            res.append(count)
        return res
# @lc code=end

