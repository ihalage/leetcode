class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ## we create a Trie (prefix tree) with the words in our list.
        ## then we start dfs at every location of the grid and check whether the current character has any children
        ## if not then backtrack. if yes, then continue to next char and check whether this is in the children of current node of Trie
        ## as soon as we find a leaf node, ie. self.is_word = True then we add it to result set
        
        root = TrieNode()
        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set() # result is a set because we don't want duplicates

        def dfs(r, c, trieNode, curWord):
            if ((r>=ROWS) or 
                (r<0) or 
                (c>=COLS) or 
                (c<0) or
                (r, c) in visit or
                board[r][c] not in trieNode.children):
                return

            visit.add((r, c))
            trieNode = trieNode.children[board[r][c]]
            curWord += board[r][c]
            
            if trieNode.is_word: # we found a solution
                res.add(curWord)

            dfs(r-1, c, trieNode, curWord)
            dfs(r+1, c, trieNode, curWord)
            dfs(r, c-1, trieNode, curWord)
            dfs(r, c+1, trieNode, curWord)
            
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return res

            

        
