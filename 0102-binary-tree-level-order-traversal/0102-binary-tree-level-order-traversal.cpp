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
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        deque<TreeNode*> q;
        if (root) q.push_back(root);
        vector<vector<int>> ans;
        while (!q.empty()) {
            vector<int> level;
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* cur = q.front();
                level.push_back(cur->val);
                q.pop_front();
                if (cur->left) q.push_back(cur->left);
                if (cur->right) q.push_back(cur->right);
            }
            ans.push_back(level);
        }
        return ans;
    }
};