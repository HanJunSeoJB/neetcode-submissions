class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(lst: List) -> bool:
            checklst = [False] * 10
            for num in lst:
                if num == '.':  continue
                if checklst[int(num)]:
                    return False
                checklst[int(num)] = True
            return True
        
        for row in board:
            if not check(row):
                print(row)
                return False

        transposed = [list(row) for row in zip(*board)]

        for row in transposed:
            if not check(row):
                print(row)
                return False
        
        n = len(board)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                sub_box = [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
                if not check(sub_box):
                    return False
        
        return True