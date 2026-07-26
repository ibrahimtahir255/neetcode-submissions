# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_val, max_val):

            # base case
            if not node:
                return True

            if  min_val < node.val < max_val:
                left_tree = dfs(node.left, min_val, node.val)
                right_tree = dfs(node.right, node.val, max_val)
            else:
                return False

            if left_tree and right_tree:
                return True        
            else:
                return False    

        return dfs(root, -float('inf'), float('inf'))
        