class Solution:
    """
    We have a recursive function that takes arguments (row, cur_board). Within the recursive function we loop through
    columns from 0 to n. For each column we check if it is safe to place a queen in that column. If not, we move to the 
    next column. If it is safe, we add  that position to current board and increase the row number in the recursive call
    to find a safe position in the next row. We then backtrack by removing the added position from the board and continue.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        ## function to check if a position is safe
        def is_safe(prev_placements: List, cur_placement):
            safe = True
            for loc in prev_placements:
                if cur_placement[0]==loc[0] or cur_placement[1]==loc[1] or (abs(cur_placement[0]-loc[0])==abs(cur_placement[1]-loc[1])): ## same row, col or diagonal
                    safe = False
            return safe

        def print_solution(sols: List):
            output = []
            for sol in sols:
                board = [["."]*n for _ in range(n)]
                for q in sol:
                    board[q[0]][q[1]] = 'Q'
                board = [''.join(row) for row in board]
                output.append(board)
            return output

        result = []
        def solve_backtrack(row, cur_board):
            if row==n:
                result.append(cur_board[:])
                return
            for col in range(n):
                safe = is_safe(cur_board, [row, col])
                if safe:
                    cur_board.append([row, col]) 
                    solve_backtrack(row+1, cur_board)
                    cur_board.pop()

            return

        solve_backtrack(0, [])
        output = print_solution(result)

        return output
