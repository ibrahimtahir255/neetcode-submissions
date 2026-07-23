from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # intialize a queue
        queue = deque()
        # initialize a good node count
        count = 0

        queue.append((root, root.val))

        # while loop whwn the queue is not empty
        while queue:
            level_size = len(queue)
            # for loop to iterate over nodes on this level
            for i in range (level_size):
                # pop the node from the queue
                node, max_so_far = queue.popleft()

                if node.val >= max_so_far:
                    count += 1 
                # compare to max and asign
                max_so_far = max(node.val, max_so_far)

                # add to queue bith the node and its max
                if node.left:
                    queue.append((node.left, max_so_far))
                if node.right:
                    queue.append((node.right, max_so_far))
        return count
            


        