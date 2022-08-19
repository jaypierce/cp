class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        out = []
        def inorder(root):
            if not root:
                return root
            
            inorder(root.left)
            out.append(root.val)
            inorder(root.right)
            
            return out
        
        def toTree(root, out):
            if not out:
                return None
            
            mid = len(out) // 2
            
            root = TreeNode(out[mid])
            root.left = toTree(root.left, out[:mid])
            root.right = toTree(root.right, out[mid+1:])
            
            return root
        
        if not root:
            return TreeNode(val)
        out = inorder(root)
        bisect.insort(out, val)
        return toTree(TreeNode(), out)
        
#         if not root:
#             return TreeNode(val)
        
#         if root.val < val:
#             root.right = self.insertIntoBST(root.right, val)
#         else:
#             root.left = self.insertIntoBST(root.left, val)
        
#         return root