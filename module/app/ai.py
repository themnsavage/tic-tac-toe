from module.app.game_board import Game_Board
from copy import deepcopy
class AI:
    def __init__(self, game_board_object: Game_Board, game_piece="O"):
        self._game_board_object = game_board_object
        self._game_piece = game_piece
        
        self._other_player_game_piece = "X" if game_piece == "O" else "O"
        self._score_table = {
            game_piece: 1,
            self._other_player_game_piece: -1,
        }
    
    def get_best_move(self):
        best_score = None
        best_move = None

        for grid_number in range(1,10):
            if self._game_board_object.is_grid_empty(grid_number):
                self._game_board_object.add_turn_to_game_board(grid_number, self._game_piece)
                score = self._mini_max(depth=0, is_maximizing=True)
                self._game_board_object.add_turn_to_game_board(grid_number, '')

                if best_score is None or score > best_score:
                    best_score = score
                    best_move = grid_number
        
        return best_move
                
    def _mini_max(self, depth, is_maximizing):
        winner = self._game_board_object.check_for_winner()
        if winner:
            return self._score_table[winner]
        elif self._game_board_object.is_game_board_filled():
            return 0
        
        if is_maximizing:
            return self._maximize_score(depth)
        else:
            return self._minimize_score(depth)

    def _maximize_score(self, depth):
        best_score = None

        for grid_number in range(1,10):
            if self._game_board_object.is_grid_empty(grid_number):
                self._game_board_object.add_turn_to_game_board(grid_number, self._game_piece)
                score = self._mini_max(depth + 1, False)
                self._game_board_object.add_turn_to_game_board(grid_number, '')
                
                if best_score is None or score > best_score:
                    best_score = score
        
        return best_score

    def _minimize_score(self,depth):
        best_score = None

        for grid_number in range(1,10):
            if self._game_board_object.is_grid_empty(grid_number):
                self._game_board_object.add_turn_to_game_board(grid_number, self._other_player_game_piece)
                score = self._mini_max(depth + 1, True)
                self._game_board_object.add_turn_to_game_board(grid_number, '')
                
                if best_score is None or score < best_score:
                    best_score = score
        
        return best_score