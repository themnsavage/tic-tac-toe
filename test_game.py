import pytest
from game import Game

def test_game_init():
    player1_name = 'Noah'
    player2_name = 'Reed'
    default_game_board = [
                        ['','',''],
                        ['','',''],
                        ['','','']
                        ]        

    game_object = Game(player1_name, player2_name)
    
    assert game_object._player1_name ==  player1_name
    assert game_object._player2_name == player2_name
    assert game_object._game_board == default_game_board


def test_get_game_board():
    default_game_board = [
                        ['','',''],
                        ['','',''],
                        ['','','']
                        ]

    game_object = Game()

    assert default_game_board == game_object.get_game_board()


def test_get_player_names():
    player1_name = 'Noah'
    player2_name = 'Reed'

    game_object = Game(player1_name, player2_name)

    assert player1_name == game_object.get_player1_name()
    assert player2_name == game_object.get_player2_name()


def test_add_turn_to_game_board():

    row = 0
    column = 0
    game_piece = 'X'
    updated_game_board = [
                        ['X','',''],
                        ['','',''],
                        ['','','']
                        ]

    game_object = Game()

    game_object.add_turn_to_game_board(row, column, game_piece)

    assert game_object.get_game_board() == updated_game_board




    