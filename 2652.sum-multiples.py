#
# @lc app=leetcode id=2652 lang=python3
#
# [2652] Sum Multiples
#

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for num in range(1,n+1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                sum += num
        return sum        
# @lc code=end

