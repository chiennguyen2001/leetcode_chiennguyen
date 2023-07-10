#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] > max_diff and nums[j] > nums[i]:
                    max_diff = nums[j] - nums[i]
        return max_diff
# @lc code=end

