#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums.index(max(nums))
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        i = 0
        while i < len(nums) - 2:
            arr = nums[i:i+3]
            if max(arr) == arr[1]:
                return i + 1
            else:
                i += 1
# @lc code=end

