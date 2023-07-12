#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
# @lc code=end

