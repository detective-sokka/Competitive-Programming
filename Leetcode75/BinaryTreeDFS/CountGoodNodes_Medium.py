### Note: Immutability of integer object in python causes time taken to increase. Consider using a list instead as it is mutable ###

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 1
        maxValue = root.val - 1

        def findGoodNodes(root, maxNodeValue, result):
            if root is not None:
                if root.val >= maxNodeValue:
                    result = result + 1
                    maxNodeValue = root.val

                result = findGoodNodes(root.left, maxNodeValue, result)
                result = findGoodNodes(root.right, maxNodeValue, result)

            return result
        
        return findGoodNodes(root, maxValue, 0)