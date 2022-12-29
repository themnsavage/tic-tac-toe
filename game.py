class Game:
    def __init__(self, player1_name, player2_name): 
        self._game_board = [['','',''],
                            ['','',''],
                            ['','','']
                            ]        
        self._player1_name = player1_name
        self._player2_name = player2_name
