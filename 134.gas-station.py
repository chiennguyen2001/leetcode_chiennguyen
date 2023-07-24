#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1

        current_cost = 0 
        start = 0
        for i in range(len(gas)):
            current_cost += gas[i] - cost[i]
            if current_cost < 0:
                current_cost = 0
                start = i+1

        return start        
# @lc code=end

