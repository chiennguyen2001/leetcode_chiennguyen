#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = []
        total = 0
        for i in nums:
            total += i
            rs.append(total)
        return rs
# @lc code=end

