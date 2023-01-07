import pytest
from unittest.mock import patch
from module.app.game_board import Game_Board
from module.app.ai import AI

def test_init():
    current_game_board = [
                ['X','O',''],
                ['','X','X'],
                ['O','O','']
                ]
    game_board_added_on = [
                ['X','O','X'],
                ['','X','X'],
                ['O','O','']
                ]
    old_board_object = Game_Board()
    old_board_object._game_board = current_game_board

    ai_object = AI(game_board_object=old_board_object)

    assert ai_object._game_board_object._game_board == current_game_board

    old_board_object.add_turn_to_game_board(3, 'X')
    assert ai_object._game_board_object._game_board == game_board_added_on

@patch('module.app.ai.AI._mini_max')
def test_get_best_move(mock_mini_max):
    ai_game_piece = 'O'
    excepted_best_move = 9
    scores = [1,2,3,4,5,6,7,8,9]
    game_board_object = Game_Board() #empty game board

    mock_mini_max.side_effect = scores
    ai_object = AI(game_board_object, ai_game_piece)
    
    assert excepted_best_move == ai_object.get_best_move()

def test_get_best_move_no_mocks():
    current_game_board = [
            ['X','',''],
            ['X','O',''],
            ['O','','']
            ]
    ai_game_piece = 'X'
    best_move = 3
    game_board = Game_Board()

    game_board._game_board = current_game_board
    ai_player = AI(game_board, ai_game_piece)

    assert best_move == ai_player.get_best_move()






