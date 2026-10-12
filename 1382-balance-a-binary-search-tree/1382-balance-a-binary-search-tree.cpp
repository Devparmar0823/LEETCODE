/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    void storeInorder(TreeNode* root, vector<TreeNode*>& nodes) {
        if (!root) return;
        storeInorder(root->left, nodes);
        nodes.push_back(root);
        storeInorder(root->right, nodes);
    }
    TreeNode* buildBalancedBST(vector<TreeNode*>& nodes, int start, int end) {
        if (start > end) return nullptr;
        int mid = start + (end - start) / 2;
        TreeNode* root = nodes[mid];
        root->left = buildBalancedBST(nodes, start, mid - 1);
        root->right = buildBalancedBST(nodes, mid + 1, end);

        return root;
    }

public:
    TreeNode* balanceBST(TreeNode* root) {
        vector<TreeNode*> nodes;
        storeInorder(root, nodes);
        return buildBalancedBST(nodes, 0, nodes.size() - 1);
    }
};
