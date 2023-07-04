#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = 0
        i = len(nums) - 1
        while i > 0:
        # for i in range(len(nums) - 2):
            if nums[i] - nums[i - 1] >= max_diff:
                max_diff = nums[i] - nums[i - 1]
            i -= 1
        return max_diff
# @lc code=end

