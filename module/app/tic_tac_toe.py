from module.app.game_board import Game_Board

class Tic_Tac_Toe:
    def __init__(self):
        self._player_dict = {
            "player 1": "X",
            "player 2": "O"
        }
        self._game_board_object = Game_Board()
    
    def start(self):
        self._print_instructions()
        keeping_playing = True
        while(keeping_playing):
            for player, game_piece in self._player_dict.items():
                self._print_current_game_board()
                self._print_guide_game_board()
                
                print(f"{player} turn:")
                current_player_turn = self._get_player_turn()
                self._game_board_object.add_turn_to_game_board(current_player_turn, game_piece)
                
                if self._game_board_object.check_for_winner():
                    print(f"{player} has won")
                    self._game_board_object.print_game_board()
                    keeping_playing = False
                    break
                elif self._game_board_object.is_game_board_filled():
                    print('board is filled tie')
                    self._game_board_object.print_game_board()
                    keeping_playing = False
                    break

    def _print_instructions(self):
        print('Instruction: Wait for your turn and use the guide game board and current board to decide your turn.')
    
    def _print_current_game_board(self):
        print('Current Game Board:')
        self._game_board_object.print_game_board()

    def _print_guide_game_board(self):
        print('Guide Game Board:')
        self._game_board_object.print_guide_game_board()

    def _get_player_turn(self):
        not_valid_turn = True

        while(not_valid_turn):
            player_turn = input('input turn based on guide game board:')

            try:
                player_turn = int(player_turn)
                
                if player_turn >= 1 and player_turn <= 9:
                    if self._game_board_object.is_grid_empty(player_turn):
                        not_valid_turn = False
                    else:
                        print("The grid you chose is already chosen")
                else:
                    print("Invalid Turn: please input a whole number")
            
            except Exception:
                print('Invalid Turn: please input a number')
            print('\n')
        return player_turn   