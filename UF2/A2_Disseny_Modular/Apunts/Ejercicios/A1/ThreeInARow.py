def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def check_winner(board):
    # Verificar files i columnes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Verificar diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    game_over = False

    print("Benvingut al joc del tres en ratlla!\n")

    while not game_over:
        print_board(board)
        print(f"Torn del jugador {players[current_player]}")

        # Demanar moviment del jugador
        valid_move = False
        while not valid_move:
            try:
                col, row = map(int, input("> ").split())
                if board[row][col] != ' ':
                    print("Aquesta casella ja està ocupada. Tria una altra.")
                else:
                    valid_move = True
            except (ValueError, IndexError):
                print("Entrada invàlida. Introdueix dues coordenades separades per espai (columna fila).")

        board[row][col] = players[current_player]

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Guanyen les {winner}!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("La partida ha acabat en empat.")
            game_over = True

        current_player = (current_player + 1) % 2


if __name__ == "__main__":
    main()
