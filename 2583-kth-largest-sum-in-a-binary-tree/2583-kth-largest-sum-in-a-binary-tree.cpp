#include <queue>
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        if (!root) return -1;
        
        std::vector<long long> levelSums;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int levelSize = q.size();
            long long currentLevelSum = 0;
            
            for (int i = 0; i < levelSize; ++i) {
                TreeNode* curr = q.front();
                q.pop();
                
                currentLevelSum += curr->val;
                
                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }
            levelSums.push_back(currentLevelSum);
        }
        if (levelSums.size() < k) return -1;
        std::nth_element(levelSums.begin(), levelSums.end() - k, levelSums.end());
        
        return *(levelSums.end() - k);
    }
};
