import pytest
from app.tic_tac_toe import Tic_Tac_Toe

def test_tic_tac_toe_init():
    expected_player_dict = {
            "player 1": "X",
            "player 2": "O"
        }

    tic_tac_toe_object = Tic_Tac_Toe()

    assert expected_player_dict == tic_tac_toe_object._player_dict