#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        len_rs = 0
        for i in set(s):
            counter[i] = s.count(i)
        
        for i in counter.values():
            if i%2 == 0:
                len_rs += i
            else:
                if len_rs % 2 == 0:
                    len_rs += i
                else: 
                    len_rs += i-1
        return len_rs  
# @lc code=end

