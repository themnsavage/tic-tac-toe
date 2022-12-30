import pytest
from unittest.mock import patch
from module.app.tic_tac_toe import Tic_Tac_Toe

def test_tic_tac_toe_init():
    expected_player_dict = {
            "player 1": "X",
            "player 2": "O"
        }

    tic_tac_toe_object = Tic_Tac_Toe()

    assert expected_player_dict == tic_tac_toe_object._player_dict

def test_print_instructions():
    tic_tac_toe_object = Tic_Tac_Toe()
    tic_tac_toe_object._print_instructions()
    pass

def test_print_current_game_board():
    tic_tac_toe_object = Tic_Tac_Toe()
    tic_tac_toe_object._print_current_game_board()
    pass

def test_print_guide_game_board():
    tic_tac_toe_object = Tic_Tac_Toe()
    tic_tac_toe_object._print_guide_game_board()
    pass

@patch('builtins.input')
def test_get_player_turn(mock_input):
    inputs = ['', "hello",0,10,'2']
    expected_player_turn = 2

    mock_input.side_effect = inputs
    tic_tac_toe_object = Tic_Tac_Toe()
    player_turn = tic_tac_toe_object._get_player_turn()

    print(player_turn)
    assert  expected_player_turn == player_turn
