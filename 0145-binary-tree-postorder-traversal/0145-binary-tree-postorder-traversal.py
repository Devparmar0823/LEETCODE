# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
            
        result = []
        stack = [root]
        
        # Traverse the tree and push nodes to the stack
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push left child first so right child is processed first in next iteration
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        # The result array currently holds: Root -> Right -> Left
        # Reversing it gives the true Post-order traversal: Left -> Right -> Root
        return result[::-1]
