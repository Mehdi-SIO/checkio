import unittest
import even_last

class EvenLastTest(unittest.TestCase):
	def test_checkio_with_even_numbers_array_returns_30(self):
		result = even_last.checkio([0, 1, 2, 3, 4, 5])
		self.assertEquals(30, result)

	def test_checkio_with_odd_numbers_array_returns_30(self):
		result = even_last.checkio([1, 3, 5])
		self.assertEquals(30, result)

	def test_checkio_with_single_number_array_returns_36(self):
		result = even_last.checkio([6])
		self.assertEquals(36, result)


	def test_checkio_with_empty_array_returns_zero(self):
		result = even_last.checkio([])
		self.assertEquals(0, result)



if __name__ == '__main__':
	unittest.main()
