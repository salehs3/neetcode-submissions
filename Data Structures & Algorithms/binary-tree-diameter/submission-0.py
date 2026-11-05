# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd = 0
        self.height(root)
        return self.maxd

    def height(self, root: Optional[TreeNode]) -> int:
         
        if (not root):
            return -1
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        diameter = lh+rh+2
        self.maxd = max(self.maxd,diameter)

        return 1 + max(lh,rh)
        