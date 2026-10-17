from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # Return an empty list if the tree has no nodes
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True  # Flag to track the direction of the current level
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Always add children from left to right for standard BFS queue order
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # If the direction is right-to-left, reverse the current level list
            if not left_to_right:
                current_level.reverse()
                
            result.append(current_level)
            left_to_right = not left_to_right  # Flip direction for the next level
            
        return result
