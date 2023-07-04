#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root

        find_left = self.lowestCommonAncestor(root.left, p, q)
        find_right = self.lowestCommonAncestor(root.right, p, q)

        if find_left == None:
            return find_right
        elif find_right == None:
            return find_left
        else:
            return root
# @lc code=end

