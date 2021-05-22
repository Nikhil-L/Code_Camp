
import unittest
from code_camp_1 import isSubsetSum

class SubsetSum(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_subset_0(self):
		self.assertEqual(isSubsetSum([], 0, 10), -1)

	def test_subset_1(self):
		self.assertEqual(isSubsetSum([5], 1, 5), 1)

	def test_subset_2(self):
		self.assertEqual(isSubsetSum([5, 3, 4, 11], 4, 9), 1)

	def test_subset_3(self):
		self.assertEqual(isSubsetSum([5, 3, 4, 11], 4, 6), -1)

if __name__ == '__main__':
	unittest.main()