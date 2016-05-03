import unittest
import most_wanted_letter

class MostWantedLetterTest(unittest.TestCase):
	def test_checkio_with_helloworld_returns_l(self):
		result = most_wanted_letter.checkio(u"Hello World!")
		self.assertEquals("l", result)

	def test_checkio_with_howdoyoudo_returns_o(self):
		result = most_wanted_letter.checkio(u"How do you do?")
		self.assertEquals("o", result)

	def test_checkio_with_upper_case_letter_then_use_their_lower_equivalent(self):
		result = most_wanted_letter.checkio(u"Oops!")
		self.assertEquals("o", result)

if __name__ == '__main__':
	unittest.main()
