
import unittest
from unittest.mock import patch
from code_camp_2 import JsonParser

class JsonParserTesting(unittest.TestCase):

	def setUp(self):
		self.url = 'https://en.wikipedia.org/w/api.php?format=json&action=query&titles=SMALL&prop=revisions&rvprop=content'

	def tearDown(self):
		pass

	def test_print_data(self):
		pass


	def test_get_pageid(self):
		parser = JsonParser(self.url)
		with patch.object(JsonParserTesting, "__init__", self.url) as mocked_get_pageid:

			page_id = parser.get_pageid()
			self.assertEqual(page_id, '1808130')

	def test_get_info(self):
		parser = JsonParser()
		self.assertEqual(parser.get_info(), "Done")


if __name__ == '__main__':
	unittest.main()