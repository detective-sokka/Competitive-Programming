#include <vector>

/**
 * Definition for a binary tree node.
 */

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
    void findLeafSequence(TreeNode* root, std::vector<int>& sequence){
        if (root->left == nullptr && root->right == nullptr){
            sequence.push_back(root->val);
        }

        if (root->left)
            findLeafSequence(root->left, sequence);
        if (root->right)
            findLeafSequence(root->right, sequence);
    }
    
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        std::vector<int> leafSequence1;
        findLeafSequence(root1, leafSequence1);

        std::vector<int> leafSequence2;
        findLeafSequence(root2, leafSequence2);

        return  leafSequence1 == leafSequence2;
    }
};

int main(){
    return 0;
}