#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_subArr = sum(arr)
        i = 0
        while i+2 < len(arr):
            j = i+2
            while j < len(arr):
                sum_subArr += sum(arr[i:j+1])
                j += 2
            i += 1
        return sum_subArr        
# @lc code=end

