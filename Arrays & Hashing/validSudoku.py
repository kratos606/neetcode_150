class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        squares = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if (i // 3, j // 3) not in squares:
                    squares[(i // 3, j // 3)] = set()

                if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in squares[(i // 3, j // 3)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])

        return True

