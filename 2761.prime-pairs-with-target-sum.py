#
# @lc app=leetcode id=2761 lang=python3
#
# [2761] Prime Pairs With Target Sum
#

# @lc code=start
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n+1)
        for i in range(2, n//2 + 1):
            if prime[i]:
                for j in range(i**2, n+1, i):
                    prime[j] = False

        rs = []
        for i in range(2,n//2 + 1):
            if prime[i] and prime[n-i]:
                rs.append([i, n-i])

        return rs

# @lc code=end

