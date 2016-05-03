import unittest
import median

class MedianTest(unittest.TestCase):
	def test_checkio_with_sorted_array_odd_length_returns_3(self):
		result = median.checkio([1, 2, 3, 4, 5])
		self.assertEquals(3, result)

	def test_checkio_with_not_sorted_array_odd_length_returns_3(self):
		result = median.checkio([1, 2, 3, 4, 5])
		self.assertEquals(3, result)

	def test_checkio_with_not_sorted_array_odd_length_not_following_numbers_returns_2(self):
		result = median.checkio([1, 300, 2, 200, 1])
		self.assertEquals(2, result)

	def test_checkio_with_not_sorted_array_even_length_returns_12_dot_5(self):
		result = median.checkio([3, 6, 20, 99, 10, 15])
		self.assertEquals(12.5, result)

	def test_checkio_with_not_sorted_array_even_length_returns_499999_dot_5(self):
		result = median.checkio(range(1000000))
		self.assertEquals(499999.5, result)

if __name__ == '__main__':
	unittest.main()
