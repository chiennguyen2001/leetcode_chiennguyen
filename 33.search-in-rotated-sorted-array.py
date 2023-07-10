#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target in nums:
            while right >= left:
                if target == nums[right]:
                    return right
                elif target == nums[left]:
                    return left
                elif target < nums[right]:
                    right -= 1
                elif target > nums[left]:
                    left += 1
        return -1
# @lc code=end

