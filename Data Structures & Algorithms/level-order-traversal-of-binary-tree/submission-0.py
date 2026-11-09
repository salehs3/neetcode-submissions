# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root == None):
            return []
        queue = [root]
        result = []

        while queue:
            level = []
            level_size = len(queue) 
            for i in range(level_size) :
                
                popped = queue.pop(0) 
                level.append(popped.val)
                if (popped.left): 
                    queue.append(popped.left)  
                if (popped.right):
                    queue.append(popped.right)   
                
            result.append(level)

        return result
        