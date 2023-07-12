#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)/2
        num_candyType = len(set(candyType))
        return int(min(n,num_candyType))
# @lc code=end

