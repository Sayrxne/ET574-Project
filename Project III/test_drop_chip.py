import unittest
from main import Connect4

class Connect4DropChipTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_drop_chip_success(self):
        # Test dropping a chip into an empty column
        result = self.game.drop_chip(3)
        self.assertTrue(result)
        self.assertEqual(self.game.board[5][2], self.game.current_player)

    def test_drop_chip_full_column(self):
        column = 2
        # Fill the column
        for _ in range(6):
            self.game.drop_chip(column)
            self.game.switch_player()
        result = self.game.drop_chip(column)
        self.assertFalse(result)

    def test_drop_chip_invalid_column(self):
        # Test dropping a chip into an invalid column
        column = 8
        result = self.game.drop_chip(column)
        self.assertFalse(result)

    def test_drop_chip_full_board(self):
        # Fill the entire board
        for column in range(7):
            for _ in range(6):
                self.game.drop_chip(column)
                self.game.switch_player()
        result = self.game.drop_chip(1)
        self.assertFalse(result)

    # my tests 
    # correctly switches players after a chip is dropped
    def test_switch_player(self):
        self.game.drop_chip(1)
        self.game.switch_player()
        self.assertTrue(self.game.drop_chip(1))
        self.assertEqual(self.game.board[4][0], 'O')


    # chips are correctly stacked in a column, one on top of the other
    def test_column_stacking(self):
        column = 2
        self.assertTrue(self.game.drop_chip(column))
        self.assertEqual(self.game.board[5][column], self.game.current_player)

        self.game.switch_player()
        self.assertTrue(self.game.drop_chip(column))
        self.assertEqual(self.game.board[4][column], self.game.current_player)

if __name__ == '__main__':
    unittest.main()