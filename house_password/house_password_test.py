import unittest
import house_password

class HousePasswordTest(unittest.TestCase):
	def test_checkio_with_password_length_lower_than_ten_returns_false(self):
		result = house_password.checkio(u'A1213pokl')
		self.assertEquals(False, result)

	def test_checkio_with_good_password_first_example_returns_true(self):
		result = house_password.checkio(u'bAse730onE4')
		self.assertEquals(True, result)

	def test_checkio_with_only_lower_case_letters_returns_false(self):
		result = house_password.checkio(u'asasasasasasasaas')
		self.assertEquals(False, result)

	def test_checkio_with_only_lower_case_letters_returns_false(self):
		result = house_password.checkio(u'asasasasasasasaas')
		self.assertEquals(False, result)

	def test_checkio_with_no_figures_returns_false(self):
		result = house_password.checkio(u'QWERTYqwerty')
		self.assertEquals(False, result)

	def test_checkio_with_no_letters_returns_false(self):
		result = house_password.checkio(u'123456123456')
		self.assertEquals(False, result)

	def test_checkio_with_good_password_second_example_returns_true(self):
		result = house_password.checkio(u'QwErTy911poqqqq')
		self.assertEquals(True, result)


if __name__ == '__main__':
	unittest.main()
