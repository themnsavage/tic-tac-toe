class Game:
    def __init__(self, player1_name = "player 1", player2_name = "player 2"): 
        self._game_board = [['','',''],
                            ['','',''],
                            ['','','']
                            ]        
        self._player1_name = player1_name
        self._player2_name = player2_name


    def get_game_board(self):
        return self._game_board

    
    def get_player1_name(self):
        return self._player1_name

    def get_player2_name(self):
        return self._player2_name

    def add_turn_to_game_board(self, row, column, game_piece):
        self._game_board[row][column] = game_piece

    def print_game_board(self):
        print(self._create_draw_game_board())
    
    def print_guide_game_board(self):
        guide_game_board = "|  1  |  2  |  3  |     \n ----- ----- -----\n|  4  |  5  |  6  |     \n ----- ----- -----\n|  7  |  8  |  9  |     \n"
        print(guide_game_board)

    def _is_game_board_filled(self):
        for row in self._game_board:
            for element in row:
                if element == '':
                    return False
        
        return True

    def _create_draw_game_board(self):
        self._draw_board = ""
        column = 0
        for i in range(5):
            if i%2 == 0:
                for row in range(3):
                    current_grid = self._game_board[column][row]
                    
                    if current_grid == 'X':
                        self._draw_board += "|  X  "
                    
                    elif current_grid == 'O':
                        self._draw_board += "|  O  "                    
                   
                    else:
                        self._draw_board += "|     "
                
                self._draw_board += "|     "
                column += 1
            else:
                self._draw_board += " -----" * 3
            self._draw_board += "\n"