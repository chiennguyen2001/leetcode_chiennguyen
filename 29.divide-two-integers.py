#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if int(dividend/divisor) > 2**31 - 1:
            return 2**31 - 1
        elif int(dividend/divisor) < -2**31:
            return -2**31 
        else:    
            return int(dividend/divisor)
# @lc code=end

