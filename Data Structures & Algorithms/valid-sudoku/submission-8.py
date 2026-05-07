class Solution:
    def isValidSudoku( self ,board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for row in range(9):
            for column in range(9):
                num = board[row][column]

                if num == ".":
                    continue

                if (num in rows[row]
                   or num in columns[column]
                   or num in grids[(row // 3, column // 3)]):
                    return False
                rows[row].add(num)
                columns[column].add(num)
                grids[(row // 3, column // 3)].add(num)
                
        return True