#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#

# @lc code=start
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
            satisfaction.sort()
            if satisfaction[-1] <= 0:
                return 0
            sum_all = []

            for i in range(1, len(satisfaction) + 1):
                arr = satisfaction[-i:]
                k = 1
                sum = 0
                for j in arr:
                    sum += j * k
                    k += 1
                sum_all.append(sum)
                
            return max(sum_all)
# @lc code=end

