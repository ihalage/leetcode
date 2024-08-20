class Solution:
    """
    Run dfs from every cell in the grid and check if the word can be formed from the current cell.
    Make sure to have a set to keep track of visited cells. Also to backtrack by popping from the set.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
                
            if ((r<0) or (r>=ROWS) or
                (c<0) or (c>=COLS) or
                (r, c) in path or
                board[r][c]!=word[i]):
                return False
                
            path.add((r, c))
            res = (dfs(r-1, c, i+1) or
                    dfs(r, c-1, i+1) or 
                    dfs(r+1, c, i+1) or
                    dfs(r, c+1, i+1))
            path.remove((r, c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                path = set()
                if dfs(r, c, 0):
                    return True
            
        return False