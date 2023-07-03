#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = sorted(nums1 + nums2)
        indx = int(len(total)/2)
        if len(total) % 2 != 0:
            return total[indx]
        else:
            return (total[indx]  + total[indx - 1]) / 2
# @lc code=end

