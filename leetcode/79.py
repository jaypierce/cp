class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c, word, visited):
            if len(word) == 0:
                return True
            
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[0] \
            or visited[(r,c)]:
                return False
            
            visited[(r,c)] = True
            
            found = False
            for i in dirs:
                if dfs(r+i[0], c+i[1], word[1:], visited):
                    found = True
            visited[(r,c)] = False
            
            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                # if board[r][c] == word[0]:
                if dfs(r,c,word,defaultdict(bool)):
                        return True
        return False