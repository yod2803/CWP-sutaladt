def is_piece(char):
    return char in "PBRQK"


def inside(board, row, col):
    size = len(board)
    return 0 <= row < size and 0 <= col < size


def ray_hits_king(board, row, col, dr, dc):
    row += dr
    col += dc


    while inside(board, row, col):
        current = board[row][col]
        if current == "K":
            return True

        if is_piece(current):
            return False

        row += dr
        col += dc
    return False


def checkmate(board):
    if not isinstance(board, str):
        return
    rows = board.splitlines()

    if len(rows) == 0:
        return
    size = len(rows[0])

    if size == 0 or len(rows) != size:
        return

    for row in rows:
        if len(row) != size:
            return
    
    king_count = 0
    for row in rows:
        for char in row:
            if char == "K":
                king_count += 1
    if king_count != 1:
        return

    for row in range(size):
        for col in range(size):
            piece = rows[row][col]
            
            if piece == "P":
                if inside(rows, row - 1, col - 1):
                    if rows[row - 1][col - 1] == "K":
                        print("Success")
                        return

                if inside(rows, row - 1, col + 1):
                    if rows[row - 1][col + 1] == "K":
                        print("Success")
                        return

            elif piece == "B":
                directions = [
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1)
                ]

                for dr, dc in directions:
                    if ray_hits_king(rows, row, col, dr, dc):
                        print("Success")
                        return
            
            elif piece == "R":
                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]

                for dr, dc in directions:
                    if ray_hits_king(rows, row, col, dr, dc):
                        print("Success")
                        return

            elif piece == "Q":
                directions = [
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1),
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]

                for dr, dc in directions:
                    if ray_hits_king(rows, row, col, dr, dc):
                        print("Success")
                        return

    print("Fail")