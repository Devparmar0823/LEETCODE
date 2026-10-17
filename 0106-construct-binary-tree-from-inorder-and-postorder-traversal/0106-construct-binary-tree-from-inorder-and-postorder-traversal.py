# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # Map values to their indices in the inorder traversal for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Start from the last element of the postorder list
        post_idx = len(postorder) - 1
        
        def array_to_tree(in_left: int, in_right: int) -> TreeNode | None:
            nonlocal post_idx
            
            # Base case: if there are no elements to construct the subtree
            if in_left > in_right:
                return None
            
            # Select the current root value from postorder and decrement pointer
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1
            
            # Locate the root index in inorder traversal to split left/right subtrees
            root_idx = inorder_map[root_val]
            
            # CRUCIAL: Build the RIGHT subtree first because postorder processes 
            # the right subtree immediately before the root when moving backward.
            root.right = array_to_tree(root_idx + 1, in_right)
            root.left = array_to_tree(in_left, root_idx - 1)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
