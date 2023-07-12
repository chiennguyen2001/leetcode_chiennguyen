#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum = 0
        for i in range(len(seats)):
            sum += abs(seats[i] - students[i])
        return sum        
# @lc code=end

