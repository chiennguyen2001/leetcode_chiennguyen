#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = str(abs(x))
        reverse_num = int(num[::-1])
        if reverse_num > 2**31 -1:
            return 0
        if x < 0:
            return -reverse_num
        else:
            return reverse_num
# @lc code=end

