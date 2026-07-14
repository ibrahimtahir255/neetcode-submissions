# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case: if root is None → return None
        if not root:
            return None

        # swap root.left and root.right
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively invert root.left
        self.invertTree(root.left)
        # recursively invert root.right
        self.invertTree(root.right)
        # return root
        return root