# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counter = 0
        self.result = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # base case
        if root is None:
            return None

        # go left
        left_tree = self.kthSmallest(root.left, k)

        # visit the current node
        self.counter+= 1
        if self.counter == k:
            self.result = root.val

        # go right
        right_tree = self.kthSmallest(root.right, k)

        return self.result

        