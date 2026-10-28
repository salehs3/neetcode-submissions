# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (not root) :
            return True
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)
        return (l and r and (abs(self.height(root.left) - self.height(root.right)) <= 1))

    def height(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)

        return 1 + max(lh,rh)
        