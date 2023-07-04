#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        arr = set(nums)
        i = 1
        while i <= len(nums):
            if i not in arr:
                res.append(i)
            i += 1
        return res
# @lc code=end

