import unittest
import inlab1

class TestInLab1Code(unittest.TestCase):

	def setUp(self): 
		return 

	# Correctness tests 

	def test_binarify_16(self):
		self.assertEqual(inlab1.binarify(16), "10000")

	def test_binarify_127(self):
		self.assertEqual(inlab1.binarify(127), "1111111")

	def test_binarify_0(self):
		self.assertEqual(inlab1.binarify(0), "0")

	def test_binarify_negative(self):
		self.assertEqual(inlab1.binarify(-16), "0")

if __name__ == '__main__':
  unittest.main()	