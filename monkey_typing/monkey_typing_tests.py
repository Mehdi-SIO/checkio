import unittest
import monkey_typing

class MonkeyTypingTest(unittest.TestCase):
	def test_count_words_with_hello_how_are_you_returns_3(self):
		result = monkey_typing.count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"})
		self.assertEquals(3, result)

	def test_count_words_with_bananas_returns_1(self):
		result = monkey_typing.count_words(u"Bananas, give me bananas!!!", {u"banana", u"bananas"})
		self.assertEquals(1, result)

	def test_count_words_with_weird_text_returns_1(self):
		result = monkey_typing.count_words(u"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {u"sum", u"hamlet", u"infinity", u"anything"})
		self.assertEquals(1, result)


if __name__ == '__main__':
	unittest.main()
