class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, path, paths):
            if root:
                if not root.left and not root.right:
                    path += str(root.val)
                    paths.append(int(path))
                root.left = dfs(root.left, path + str(root.val), paths)
                root.right = dfs(root.right, path + str(root.val), paths)
            
            return sum(paths)
        
        return dfs(root, '', [])