class Solution:
    def isValidBST(self, root) -> bool:
        
        def validateChildNodes(min_val, max_val, node):
            if node is None:
                return True
                
            if node.val <= min_val or node.val >= max_val:
                return False            

            return validateChildNodes(min_val, node.val, node.left) and validateChildNodes(node.val, max_val, node.right)
        

        return validateChildNodes(float('-inf'), float('inf'), root)

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(2, TreeNode(1), TreeNode(3))

sol = Solution()
print(sol.isValidBST(root))