#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reverse_num = num[::-1]
        if num == reverse_num:
            return True
        else:
            return False
# @lc code=end

