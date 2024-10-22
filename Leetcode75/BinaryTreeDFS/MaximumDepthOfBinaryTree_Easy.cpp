#include  <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
    int findMaxDepthRecrusion(TreeNode* root, int depth){

        if(!root)
            return depth;

        int leftDepth = findMaxDepthRecrusion(root->left, depth+1);
        int rightDepth = findMaxDepthRecrusion(root->right, depth+1);

        return std::max(leftDepth, rightDepth);
    }
    
    int maxDepth(TreeNode* root) {
        return findMaxDepthRecrusion(root, 0);
    }
};

int main()
{
    return 0;
}