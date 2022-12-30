class Game_Board:
    def __init__(self): 
        self._game_board = [['','',''],
                            ['','',''],
                            ['','','']
                            ]        

    def get_game_board(self):
        return self._game_board

    def add_turn_to_game_board(self, grid_number, game_piece):
        grid = {
            1: [0,0],
            2: [0,1],
            3: [0,2],
            4: [1,0],
            5: [1,1],
            6: [1,2],
            7: [2,0],
            8: [2,1],
            9: [2,2],
        }

        row = grid[grid_number][0]
        column = grid[grid_number][1]

        self._game_board[row][column] = game_piece

    def print_game_board(self):
        print(self._create_draw_game_board())
    
    def print_guide_game_board(self):
        guide_game_board = "|  1  |  2  |  3  |     \n ----- ----- -----\n|  4  |  5  |  6  |     \n ----- ----- -----\n|  7  |  8  |  9  |     \n"
        print(guide_game_board)

    def is_game_board_filled(self):
        for row in self._game_board:
            for element in row:
                if element == '':
                    return False
        
        return True

    def check_for_winner(self):
        horzontal_winner = self._check_winner_horizontal()
        if horzontal_winner != False: return horzontal_winner
        
        vertical_winner = self._check_winner_vertical()
        if vertical_winner != False: return vertical_winner
        
        diangle_winner = self._check_winner_diangle()
        if diangle_winner != False: return diangle_winner

        return False

        

    def _check_winner_horizontal(self):
        temp_list = []
        for row in self._game_board:
            for element in row:
                temp_list.append(element)
            
            is_temp_list_winner = self._check_possible_winner_temp_list(temp_list)

            if is_temp_list_winner != False:
                return is_temp_list_winner
            else:
                temp_list = []
        
        return False

    def _check_winner_vertical(self):
        temp_list = []

        for i in range(3):
            for z in range(3):
                temp_list.append(self._game_board[z][i])

                is_temp_list_winner = self._check_possible_winner_temp_list(temp_list)

            if is_temp_list_winner != False:
                return is_temp_list_winner
            else:
                temp_list = []

        return False

    def _check_winner_diangle(self):   
        is_temp_list_winner = self._check_possible_winner_temp_list([self._game_board[0][0],self._game_board[1][1],self._game_board[2][2]])
        if is_temp_list_winner != False:
            return is_temp_list_winner

        is_temp_list_winner = self._check_possible_winner_temp_list([self._game_board[2][0],self._game_board[1][1],self._game_board[0][2]])
        if is_temp_list_winner != False:
            return is_temp_list_winner

        return False
    def _check_possible_winner_temp_list(self, temp_list):
        prev_element = None
        winning_list = True

        for current_element in temp_list:
            if (prev_element != None and current_element != prev_element) or current_element == '':
                return False
            prev_element = current_element

        return prev_element 

    def _create_draw_game_board(self):
        self._draw_board = ""
        column = 0
        for i in range(5):
            if i%2 == 0:
                for row in range(3):
                    current_grid = self._game_board[column][row]
                    
                    if current_grid == 'X':
                        self._draw_board += "|  X  "
                    
                    elif current_grid == 'O':
                        self._draw_board += "|  O  "                    
                   
                    else:
                        self._draw_board += "|     "
                
                self._draw_board += "|     "
                column += 1
            else:
                self._draw_board += " -----" * 3
            self._draw_board += "\n"