#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        rs = []
        for i in range(1, n + 1):
            if len(arr) < len(target):
                arr.append(i)
                rs.append("Push")
            if arr[-1] != target[len(arr) - 1]:
                arr.pop()
                rs.append("Pop")
            if len(arr) == len(target):
                if arr == target:
                    return rs
                else:
                    arr.pop()
                    rs.append("Pop")
        return rs
# @lc code=end

