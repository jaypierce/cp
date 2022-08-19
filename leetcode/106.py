class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(root, inorder, postorder):
            if not inorder and not postorder:
                return root
            
            root = TreeNode(postorder[-1])
            mid = inorder.index(root.val)
            
            root.left = dfs(root.left, inorder[:mid], postorder[:mid])
            root.right = dfs(root.right, inorder[mid+1:], postorder[mid:-1])
            
            return root
            
        return dfs(TreeNode(), inorder, postorder)