# Connect 4 Game | Chasyl De Guzman

class Connect4:
  def __init__(self):
    self.board = [[' ' for _ in range(7)] for _ in range(6)]
    self.current_player = 'X'

  def switch_player(self):
    self.current_player = 'O' if self.current_player == 'X' else 'X'

  def print_board(self):
    for row in self.board:
      print('|', end='')
      for cell in row:
        print(cell, end='|')
      print()
    print('---------------')
    print(' 1 2 3 4 5 6 7')

  def drop_chip(self, column):
    """
    Drops a chip into the selected column of the Connect 4 board.

    Args:
      column (int): The column number where the chip is to be dropped. It must be between 1 and 7.

    Returns:
      bool: True if the chip was successfully dropped, False if the column is full or if the column is out of range.
    """
    # TO BE IMPLEMENTED: Check if the column is out of range. The valid column # is from 1 to 7.
    if column < 1 or column > 7:
      return False

    row = 5
    while row >= 0:
      if self.board[row][column - 1] == ' ':
        # TO BE IMPLEMENTED: Drop the current player's chip into the selected slot. This simply means mark the cell 
        # you found above to self.current_player, which is either X or O
        self.board[row][column - 1] = self.current_player
        return True
      row -= 1

    # TO BE IMPLEMENTED: If the column is full, return False. Question: what indicates the column is full?
    return False
  
  def check_win(self, player):
    """
    Check if the specified player has won the game.

    Args:
      player (str): The player to check for a win. It can be either 'X' or 'O'.

    Returns:
      bool: True if the player has won, False otherwise.
    """
    # Check horizontal
    for row in range(6):
        for col in range (4):
            if (self.board[row][col] == player and
               self.board[row][col + 1] == player and
               self.board[row][col + 2] == player and 
               self.board[row][col + 3] == player):
              return True 
            
    # Check vertical
    for row in range(3):
        for col in range (7):
            if (self.board[row][col] == player and
               self.board[row + 1][col] == player and
               self.board[row + 2][col] == player and 
               self.board[row + 3][col] == player):
               return True 
    
    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range (4):
            if (self.board[row][col] == player and
               self.board[row + 1][col + 1] == player and
               self.board[row + 2][col + 2] == player and 
               self.board[row + 3][col + 3] == player):
               return True  

    # Check diagonal (bottom-left to top-right)
    for row in range(3):
        for col in range (4):
            if (self.board[5 - row][col] == player and
               self.board[5 - row - 1][col + 1] == player and
               self.board[5 - row - 2][col + 2] == player and 
               self.board[5 - row - 3][col + 3] == player):
               return True
    return False
             
  
  def play_game(self):
    game_over = False
    while not game_over:
      self.print_board()
      print(f"Player {self.current_player}'s turn.")

      try:
        column = int(input("Enter the column number (1-7): "))
      except ValueError:
        print("Invalid input. Please enter a valid column number.")
        continue

      if not self.drop_chip(column):
        print("Column is full or out of range. Try again.")
        continue
      
      self.switch_player()

if __name__ == "__main__":
  game = Connect4()
  game.play_game()
