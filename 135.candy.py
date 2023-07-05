#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(len(candies) - 1):
            if ratings[i] > ratings[i + 1]:
                candies[i] += 1
        for i in range(len(candies) - 1, 0, -1):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        return sum(candies)
        
# @lc code=end

