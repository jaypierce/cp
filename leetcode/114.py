class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right
        root.right = root.left
        root.left = None
        
        while root.right:
            root = root.right
        root.right = tmp
        
        return root