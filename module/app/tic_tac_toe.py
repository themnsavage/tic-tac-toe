from module.app.game_board import Game_Board
from module.app.ai import AI
class Tic_Tac_Toe:
    def __init__(self):
        self._player_dict = {
            "player 1": "X",
            "player 2": "O"
        }
        self._game_board_object = Game_Board()
    
    def start(self):
        game_mode = input("Enter 1 for player vs player \nEnter 2 for player vs ai\n")
        if game_mode == '1':
            self._player_vs_player()
        else:
            self._player_vs_ai()

    def _player_vs_ai(self):
        keeping_playing = True
        ai_player = AI(self._game_board_object, self._player_dict["player 2"])

        while(keeping_playing):
            for player, game_piece in self._player_dict.items():
                if player == "player 1":
                    self._print_current_game_board()
                current_player_turn = self._get_player_turn(player) if player == "player 1" else ai_player.get_best_move()
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

    def _player_vs_player(self):
        keeping_playing = True
        while(keeping_playing):
            for player, game_piece in self._player_dict.items():
                self._print_current_game_board()
                current_player_turn = self._get_player_turn(player)
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

    def _print_current_game_board(self):
        print('Current Game Board:')
        self._game_board_object.print_game_board()

    def _get_player_turn(self, player_name):
        not_valid_turn = True

        while(not_valid_turn):
            player_turn = input(f'{player_name} enter grid number(0-9):')

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