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