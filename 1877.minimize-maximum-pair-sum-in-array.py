#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = []
        for i in range(len(nums)//2):
            pair_sum.append(nums[i] + nums[0-i-1])
        return max(pair_sum)
# @lc code=end

