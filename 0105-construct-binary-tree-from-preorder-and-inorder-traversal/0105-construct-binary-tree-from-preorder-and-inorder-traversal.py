# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Map values to their indices in the inorder traversal for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        
        def array_to_tree(in_left: int, in_right: int) -> TreeNode | None:
            nonlocal pre_idx
            
            # Base case: if there are no elements to construct the subtree
            if in_left > in_right:
                return None
            
            # Select the current root value from preorder and increment pointer
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            # Locate the root index in inorder traversal to split left/right subtrees
            root_idx = inorder_map[root_val]
            
            # Build left and right subtrees (Left must be built first because of preorder order)
            root.left = array_to_tree(in_left, root_idx - 1)
            root.right = array_to_tree(root_idx + 1, in_right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
