import random
class Board():
    '''Represents the board of tic-tac-toe'''
    ROW_LEN = 3
    COL_LEN = 3
    POSITIONS = ((0, 0, 0, 1, 0, 2),
                 (1, 0, 1, 1, 1, 2),
                 (2, 0, 2, 1, 2, 2),
                 (0, 0, 1, 0, 2, 0),
                 (0, 1, 1, 1, 2, 1),
                 (0, 2, 1, 2, 2, 2),
                 (0, 0, 1, 1, 2, 2),
                 (0, 2, 1, 1, 2, 0))
    def __init__(self):
        '''Checker is for checking if the the computer can win and if opponent
        can win. Checker is also for printing board. Score is for deciding
        what to do if the opponent and computer can't win.
        '''
        self._checker = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
        self._score = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
        self._rotation = 0
    
    def __str__(self):
        for row in self._checker:
            print(str(row))
        print('')
        for row in self._score:
            print(str(row))
        return ''
    
    def print_board(self):
        '''(Board) -> None
        Gets the physical representation of the boarding.
        '''
        # print the column numbers
        print("  0 1 2")
        # print each row
        # loop through the checker
        for row_i in range(self.ROW_LEN):
            # make a string representation of the row index
            row = str(row_i)
            # loop through the row
            for col_i in range(self.COL_LEN):
                value = self._checker[row_i][col_i]
                # add the value to the string rep of row
                # check if -1, 0, or 1
                if value == 1:
                    p_val = ' O'
                elif value == -1:
                    p_val = ' X'
                else:
                    p_val = ' .'
                row += p_val
            # print the row
            print(row)
    
    def get_score(self):
        '''(Board) -> list of list of int
        Returns the score board'''
        # empty list
        clone = []
        # add clones of the list into the empty list
        for lst in self._score:
            clone.append(lst[:])
        return clone
    
    def get_checker(self):
        '''(Board) -> list of list of int
        Returns the checker board'''
        # empty list
        clone = []
        # add clones of the list into the empty list
        for lst in self._checker:
            clone.append(lst[:])
        return clone
    
    
    def restart(self):
        '''(Board) -> None
        Resets the board to its original state'''
        self._checker[:] = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
        self._score[:] = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
    
    def change(self, row, col, is_X):
        '''(Board, int, int, bool) -> None

        Puts a token on the board. Changes the score and checker.
        '''
        # set the score in that coordinate to infinity
        self._score[row][col] = float('-inf')
        # deal with is X
        if is_X:
            self._checker[row][col] = -1
        # deal with not X
        else:
            self._checker[row][col] = 1
    
    def fill(self, row, col, is_X):
        '''(Board, int, int ,bool) ->
        Checks first if the coordinates are taken. If not, put the token in.'''
        # check the checker
        if self._checker[row][col] == 0:
            self.change(row, col, is_X)
    
    def swap(self, row1, col1, row2, col2):
        '''(Board, int, int, int, int) -> None
        Swaps two coordinates' values. Changes both attributes'''
        # swap the checker values
        (self._checker[row1][col1],
         self._checker[row2][col2]) = (self._checker[row2][col2],
                                       self._checker[row1][col1])
        # swap the score values
        (self._score[row1][col1],
         self._score[row2][col2]) = (self._score[row2][col2],
                                     self._score[row1][col1])
    
    def rotate(self):
        '''(Board) -> None
        Rotates the board 90 degrees clockwise'''
        # Rotate the sides using the swap method
        self.swap(0, 1, 1, 0)
        self.swap(1, 0, 2, 1)
        self.swap(2, 1, 1, 2)
        # rotate the corners
        self.swap(0, 0, 2, 0)
        self.swap(2, 0, 2, 2)
        self.swap(2, 2, 0, 2)
        # change the rotation
        self._rotation = (self._rotation + 1) % 4

    def reset_rotation(self):
        '''(Board) -> None
        Rotates the board to its original form
        '''
        # while loop to keep rotating
        while(self._rotation != 0):
            self.rotate()
    
    def total(self, position):
        '''(Board, tuple of int) -> int
        REQ: position must be a tuple of 6 ints
        Sums up the 3 coordinates
        '''
        row1 = position[0]
        col1 = position[1]
        row2 = position[2]
        col2 = position[3]
        row3 = position[4]
        col3 = position[5]
        c1 = self._checker[row1][col1]
        c2 = self._checker[row2][col2]
        c3 = self._checker[row3][col3]
        t = c1 + c2 + c3
        return t
    
    def will_win(self, is_X):
        '''(Board, bool) -> bool, int
        Checks if the token can win. Also gives the index representing position
        of the win
        
        (0,0)(0,1)(0,2) 0
        (1,0)(1,1)(1,2) 1
        (2,0)(2,1)(2,2) 2
        (0,0)(1,0)(2,0) 3
        (1,0)(1,1)(1,2) 4
        (2,0)(2,1)(2,2) 5
        (0,0)(1,1)(2,2) 6
        (0,2)(1,1)(2,0) 7
        '''
        # What number are we checking for?
        if is_X:
            num_check = -2
        else:
            num_check = 2
        # loop through the positions with while
        index = 0
        LENGTH = len(self.POSITIONS)
        win = False
        while(not win and index < LENGTH):
            # store the values in appropriate variables
            position = self.POSITIONS[index]
            # check the sum of the values
            if self.total(position) == num_check:
                win = True
            else:
                index += 1
            # when value is what we are looking for, use that index and exit
        return (win, index)

    def do_win(self, index):
        '''(Board, int,) -> None
        REQ: We are assuming that this index is a winning index or block
        REQ: 0 <= index < 8
        Does the winning move or blocks the losing move.
        '''
        position = self.POSITIONS[index]
        row1 = position[0]
        col1 = position[1]
        row2 = position[2]
        col2 = position[3]
        row3 = position[4]
        col3 = position[5]
        # fill the coordinates
        self.fill(row1, col1, False)
        self.fill(row2, col2, False)
        self.fill(row3, col3, False)

    def opp_change(self, row, col, is_X):
        '''(Board, int, int, bool) -> None
        REQ: row and col must be from 0 to 2
        
        Changes the board when the opponent moves. Defensive purposes'''
        self.change(row, col, True)
        # check the upper left and lower right
        if((row, col) == (0, 0) or (row, col) == (2, 2)):
            self._score[1][0] += 0.5
            self._score[1][1] += 2 
        # check the other two corners
        elif((row, col) == (0, 2) or (row, col) == (2, 0)):
            self._score[1][1] += 2
            self._score[1][2] += 0.5
        # check centre
        elif((row, col) == (1, 1)):
            self._score[0][0] += 2
            self._score[0][2] += 2
            self._score[2][0] += 2
            self._score[2][2] += 2
        # deal with the sides
        else:
            # add score to middle
            self._score[1][1] += 2
            # add score to adjacent corners
            if row == 0:
                self._score[0][0] += 1
                self._score[0][2] += 1
            elif row == 2:
                self._score[2][0] += 1
                self._score[2][2] += 1
            elif col == 0:
                self._score[0][0] += 1
                self._score[2][0] += 1
            elif col == 2:
                self._score[0][2] += 1
                self._score[2][2] += 1
    
    def check_win(self, is_X):
        '''(Board, bool) -> bool, int
        Checks if the token can win. Also gives the index representing position
        of the win
        
        (0,0)(0,1)(0,2) 0
        (1,0)(1,1)(1,2) 1
        (2,0)(2,1)(2,2) 2
        (0,0)(1,0)(2,0) 3
        (1,0)(1,1)(1,2) 4
        (2,0)(2,1)(2,2) 5
        (0,0)(1,1)(2,2) 6
        (0,2)(1,1)(2,0) 7
        '''
        # What number are we checking for?
        if is_X:
            num_check = -3
            pnt = "You win!"
        else:
            num_check = 3
            pnt = "You lose."
        # loop through the positions with while
        index = 0
        LENGTH = len(self.POSITIONS)
        win = False
        while(not win and index < LENGTH):
            # store the values in appropriate variables
            position = self.POSITIONS[index]
            # check the sum of the values
            if self.total(position) == num_check:
                win = True
                # print winning message
                print(pnt)
            else:
                index += 1
            # when value is what we are looking for, use that index and exit
        return win
    
    def check_corner(self, is_X):
        '''(Board, bool) -> int
        Checks which corner is occupied by the specified token where:
        1 2
        3 4
        are the corners. Returns the corner number. Returns 0 if there are no
        corners occupied
        '''
        # what number are we checking for?
        if is_X:
            num = -1
        else:
            num = 1
        # check every corner
        corners = [(0, 0), (0, 2), (2, 2), (2, 0)]
        is_corner = False
        ind = 0
        while(not is_corner and ind < len(corners)):
            row = corners[ind][0]
            col = corners[ind][1]
            # check if the corner is what we are checking for
            if self._checker[row][col] == num:
                is_corner = True
            ind += 1
        # if corner is not found, return 0
        if not is_corner:
            result = 0
        # if a corner is found, return the index
        else:
            result = ind
        return result
        

def defense(b):
    '''(Board) -> None
    
    Computer player plays defensively.
    '''
    # store the win or lose into meaningful variables
    (win, position) = b.will_win(False)
    (lose, position2) = b.will_win(True)
    # check if computer can win
    if win:
        b.do_win(position)
    # check if player can win
    elif lose:
        b.do_win(position2)
    else:
        lst_of_highest_scores = []
        score = b.get_score()
        # loop through each row
        for row in score:
            # add the highest number in the row
            lst_of_highest_scores.append(max(row))
        # get the highest of the highest scores
        highest = max(lst_of_highest_scores)
        # create empty list to store the coords with the highest score
        choices = []
        # loop through the scores to see which coordinates are the high scores
        for r in range(len(score)):
            for c in range(len(score[r])):
                if score[r][c] == highest:
                    choices.append((r, c))
        # pick a random tuple from choices
        random.shuffle(choices)
        (row, col) = choices[0]
        # change the board using those coordinates
        b.change(row, col, False)

if __name__ == "__main__":
    b = Board()
    print("Let's play Tic-Tac-Toe!")
    play_again = True
    # this is for deciding to go defense or offense
    player_turn = True
    while(play_again):
        # when the player is first, defensive mode
        if player_turn:
            defe = True
        # when player is second, offensive mode
        else:
            defe = False
        #########################################################
        defe = True
        player_turn = True
        #########################################################
        num_turns = 0
        is_winner = False
        # loop through
        b.print_board()
        while(not is_winner and num_turns < 9):
            if player_turn:
                print("It is the player's turn.")
                str_row = input("Choose a row:")
                str_col = input("Choose a column:")
                # check if they are numbers
                if str_row.isnumeric() and str_col.isnumeric():
                    # convert to numbers
                    row = int(str_row)
                    col = int(str_col)
                    # check if in range
                    row_in_range = (row >= 0) and (row <= 2)
                    col_in_range = (col >= 0) and (col <= 2)
                    if row_in_range and col_in_range:
                        # check if space is occupied
                        check_board = b.get_checker()
                        if check_board[row][col] == 0:
                            b.opp_change(row, col, True)
                            # change who's turn it is and increase num of turns
                            player_turn = not player_turn
                            num_turns += 1
                        else:
                            print("That space is already occupied.")
                    else:
                        print("Choose a number from 0-2")
                else:
                    print("Choose a number from 0-2")
            # bot decision
            else:
                # when defense mode is on
                if defe:
                    # do defensive move
                    defense(b)
                    player_turn = not player_turn
                    num_turns += 1
            # check if there is a winner
            b.print_board()
            is_winner = b.check_win(True) or b.check_win(False)
        understood = False
        while(not understood):
            ask = input("Do you want to play again? y/n\n")
            if ask == 'y':
                print("Let's play again!")
                
                understood = True
            elif ask == 'n':
                print("Alright. You should study now.")
                play_again = False
                understood = True
            else:
                print("I didn't quite hear that.")