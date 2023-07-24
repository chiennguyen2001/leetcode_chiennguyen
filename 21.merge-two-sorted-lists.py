#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        rs = out
        while list1 and list2:
            if list1.val < list2.val:
                rs.next = list1
                list1 = list1.next
            else:
                rs.next = list2
                list2 = list2.next
            rs = rs.next
        
        if list1:
            rs.next = list1
        if list2:
            rs.next = list2

        return out.next   
# @lc code=end

