#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = set(nums)
        for i in arr:
            if nums.count(i) == 1:
                return i
# @lc code=end

