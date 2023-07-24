#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0,1], [-1,0], [0,-1], [1,0]]
        cur = [0, 0]
        i = 0
        for _ in range(4):
            for ch in instructions:
                if i == 4 or i == -4:
                    i = 0
                if ch == "G":
                    cur[0] += direction[i][0]
                    cur[1] += direction[i][1]
                elif ch == "L":
                    i += 1
                else:
                    i -= 1
            if cur == [0, 0]:
                return True
        
        return False        
        
# @lc code=end

