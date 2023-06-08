# unittest - python module with unit testing framework
# unit testing - common conception of testing small pices of your code
import upper
import unittest
 
class TestUpper(unittest.TestCase):
  def test_one_word(self):
    text = 'hello!'
    result = upper.upper_text(text)
    self.assertEqual(result,'Hello!')
    
  def test_multiple_words(self):
    result = upper.upper_text('hello world!')
    self.assertEqual(result, 'Hello World!')
      

if __name__ == '__main__':
	unittest.main()


