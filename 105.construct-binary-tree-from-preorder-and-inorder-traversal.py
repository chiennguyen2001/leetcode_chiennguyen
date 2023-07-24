#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder.pop(0))

        root.left = self.buildTree(preorder,inorder[:root_idx])
        root.right = self.buildTree(preorder,inorder[root_idx + 1:])

        return root
# @lc code=end

