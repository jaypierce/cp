# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        out = []
        queue = []
        
        def bfs(node):
            if not node:
                return node
            
            queue.append(node)
            out.append([node.val])
            
            while queue:
                lis = []
                l = len(queue)
                
                for _ in range(l):
                    n = queue.pop(0)
                    if n.left:
                        queue.append(n.left)
                        lis.append(n.left.val)
                    if n.right:
                        queue.append(n.right)
                        lis.append(n.right.val)
                if lis:
                    out.append(lis)
                    
            return out
        
        return bfs(root)