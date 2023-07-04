#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        rs = []
        for i in set(nums):
            if nums.count(i) == 1:
                rs.append(i)
        return rs
# @lc code=end

