#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ""
        for i in digits:
            num_str += str(i)
        num_str = int(num_str) + 1
        arr = [int(x) for x in str(num_str)]
        return arr
            
        
# @lc code=end

