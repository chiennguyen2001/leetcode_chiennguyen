#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rs = []
        for i in range(0, (len(nums) - 1)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    rs.append(i)
                    rs.append(j)
                    return rs
# @lc code=end
