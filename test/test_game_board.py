import pytest
from app.game_board import Game_Board

def test_game_board_init():
    default_game_board = [
                        ['','',''],
                        ['','',''],
                        ['','','']
                        ]        

    game_object = Game_Board()

    assert game_object._game_board == default_game_board


def test_get_game_board():
    default_game_board = [
                        ['','',''],
                        ['','',''],
                        ['','','']
                        ]

    game_object = Game_Board()

    assert default_game_board == game_object.get_game_board()

def test_add_turn_to_game_board():
    grid_number = 4
    game_piece = 'X'
    updated_game_board = [
                        ['','',''],
                        ['X','',''],
                        ['','','']
                        ]

    game_object = Game_Board()

    game_object.add_turn_to_game_board(grid_number, game_piece)

    assert game_object.get_game_board() == updated_game_board

def test_create_empty_draw_board():
    empty_draw_board = "|     |     |     |     \n ----- ----- -----\n|     |     |     |     \n ----- ----- -----\n|     |     |     |     \n"
    

    game_object = Game_Board()
    game_object._create_draw_game_board()

    assert empty_draw_board == game_object._draw_board


def test_create_filled_draw_board():
    filled_draw_board = "|  X  |  O  |     |     \n ----- ----- -----\n|     |  X  |  X  |     \n ----- ----- -----\n|  O  |  O  |     |     \n"
    
    game_object = Game_Board()
    game_object._game_board = [
                        ['X','O',''],
                        ['','X','X'],
                        ['O','O','']
                        ]
    game_object._create_draw_game_board()
    
    assert filled_draw_board == game_object._draw_board 

def test_print_game_board():
    game_object = Game_Board()
    game_object.print_game_board()
    pass

def test_print_guide_game_board():
    game_object = Game_Board()
    game_object.print_guide_game_board()
    pass

def test_board_is_filled():
    filled_game_board = [
                        ['X','O','O'],
                        ['O','X','X'],
                        ['O','O','X']
                        ]
    un_filled_game_board = [
                    ['X','O',''],
                    ['','X','X'],
                    ['O','O','']
                    ]

    game_object = Game_Board()
    
    game_object._game_board = filled_game_board
    assert True == game_object.is_game_board_filled()

    game_object._game_board = un_filled_game_board
    assert False == game_object.is_game_board_filled()

def test_check_possible_winner_temp_list():
    winning_list = ['X', 'X', 'X']
    losing_list = ['O', 'O', '']

    game_object = Game_Board()

    assert 'X' == game_object._check_possible_winner_temp_list(winning_list)
    assert False == game_object._check_possible_winner_temp_list(losing_list)

def test_check_winner_horizontal():
    winning_horzontal_game_board = [
                    ['X','O',''],
                    ['X','X','X'],
                    ['O','','O']
                    ]
    losing_horzontal_game_board = [
                    ['X','O',''],
                    ['X','O','X'],
                    ['X','','O']
                    ]
    
    game_object = Game_Board()

    game_object._game_board = winning_horzontal_game_board
    assert 'X' == game_object._check_winner_horizontal()

    game_object._game_board = losing_horzontal_game_board
    assert False == game_object._check_winner_horizontal()

    def test_check_winner_vertical():
        winning_vertical_game_board = [
                        ['X','O',''],
                        ['X','O','X'],
                        ['X','','O']
                        ]

        losing_vertical_game_board = [
                        ['X','O',''],
                        ['X','X','X'],
                        ['O','','O']
                        ]
        
        game_object = Game_Board()

        game_object._game_board = winning_vertical_game_board
        assert 'X' == game_object._check_winner_vertical()

        game_object._game_board = losing_vertical_game_board
        assert False == game_object._check_winner_vertical()

    def test_check_winner_diangle():
        winning_diangle_game_board = [
                        ['X','O',''],
                        ['O','X','O'],
                        ['X','','X']
                        ]

        losing_diangle_game_board = [
                        ['X','O',''],
                        ['X','X','X'],
                        ['O','','O']
                        ]
        
        game_object = Game_Board()

        game_object._game_board = winning_dianglel_game_board
        assert 'X' == game_object._check_winner_diangle()

        game_object._game_board = losing_diangle_game_board
        assert False == game_object._check_winner_diangle()

    def test_check_for_winner():
        winning_horzontal_game_board = [
                        ['X','O',''],
                        ['X','X','X'],
                        ['O','','O']
                        ]
        winning_vertical_game_board = [
                        ['X','O',''],
                        ['X','O','X'],
                        ['X','','O']
                        ]
        winning_diangle_game_board = [
                        ['X','O',''],
                        ['O','X','O'],
                        ['X','','X']
                        ]
        losing_game_board =  [
                        ['X','O','O'],
                        ['O','X','X'],
                        ['X','X','O']
                        ]

        game_object._game_board = winning_horzontal_game_board
        assert 'X' == game_object.check_for_winner()

        game_object._game_board = winning_vertical_game_board
        assert 'X' == game_object.check_for_winner()
        
        game_object._game_board = winning_diangle_game_board
        assert 'X' == game_object.check_for_winner()

        game_object._game_board = losing_game_board
        assert False == game_object.check_for_winner()           