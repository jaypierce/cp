class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in visited \
            or board[r][c] == 'X':
                return
            
            visited.add((r,c))
            board[r][c] = 'T'
            
            for i,j in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(r+i, c+j)
        
        
#         for i in range(len(board[0])):
#             if board[0][i] == 'O':
#                 dfs(0, i)
#             if board[len(board)-1][i] == 'O':
#                 dfs(len(board)-1, i)
        
#         for j in range(len(board)):
#             if board[j][0] == 'O':
#                 dfs(j, 0)
#             if board[j][len(board[0])-1] == 'O':
#                 dfs(j, len(board[0])-1)
        
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r,c)
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X" 