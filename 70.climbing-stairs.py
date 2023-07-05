#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        k = n//2
        sum = 1
        for i in range(1,k + 1):
            sum += math.comb(n-i, i)

        return sum
# @lc code=end

