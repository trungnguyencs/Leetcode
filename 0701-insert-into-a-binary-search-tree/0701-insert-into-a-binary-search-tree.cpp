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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* node = new TreeNode(val);
        if (root == NULL) return node;
        TreeNode* cur = root;
        while (cur != NULL) {
            if (cur->val > val) {
                if (cur->left != NULL) cur = cur->left;
                else {
                    cur->left = node;
                    break;
                }
            };
            if (cur->val < val) {
                if (cur->right != NULL) cur = cur->right;
                else {
                    cur->right = node;
                    break;
                }
            };
        }
        return root;
    }
};