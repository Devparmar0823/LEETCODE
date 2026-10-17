# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
            
        max_width = 0
        # Queue stores pairs of (node, positional_index)
        queue = deque([(root, 0)])
        
        while queue:
            level_length = len(queue)
            # The index of the first and last node at the current level
            _, first_idx = queue[0]
            _, last_idx = queue[-1]
            
            # Update the global maximum width
            max_width = max(max_width, last_idx - first_idx + 1)
            
            # Process all nodes at the current level
            for _ in range(level_length):
                node, idx = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
                    
        return max_width
