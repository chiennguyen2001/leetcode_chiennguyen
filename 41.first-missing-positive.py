#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 1
        if nums[-1] < 0:
            return count
        for num in nums:
            if num == count:
                count += 1
        return count

# @lc code=end

