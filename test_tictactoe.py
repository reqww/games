import sys
sys.path.insert(0, '/main')

import unittest
import check_board, game_win, write_board

x = [
	[1, 1, 2],
	[2, 2, 0],
	[2, 1, 0],
]

y = [
	[1, 2, 1],
	[1, 2, 0],
	[1, 0, 2],
]

z = [
	[1, 0, 1],
	[0, 2, 0],
	[1, 0, 2]
]

t = [
	[1, 1, 2],
	[2, 1, 1],
	[1, 2, 2]
]

class MyCalcTest(unittest.TestCase):

	def test_validation_output(self):
		self.assertIsInstance(check_board.validate_board(x), bool)

	def test_validation_output_not_right(self):
		self.assertFalse(check_board.validate_board(x))

	def test_validation_output_right(self):
		self.assertTrue(check_board.validate_board(y))

	def test_win_type(self):
		self.assertIsInstance(game_win.game_finished(x), int)

	def test_win_zero(self):
		self.assertEqual(game_win.game_finished(z), 0)

	def test_win_winner(self):
		self.assertEqual(game_win.game_finished(y), 1)

	def test_win_draw(self):
		self.assertEqual(game_win.game_finished(t), -1)

	def test_board(self):
		self.assertIsInstance(write_board.write_table(x), str)




if __name__ == "__main__":
	unittest.main()