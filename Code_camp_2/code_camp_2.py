
import json
import requests

class JsonParser:

	def __init__(self, url):
		self.base_url = 'https://en.wikipedia.org/wiki/'
		self.url = url
		self.page_id = None
		self.reference_links = []

	def get_pageid(self):
		response = requests.get(self.url)
		data = json.loads(response.text)
		self.data = data
		page_id = list(self.data['query']['pages'].keys())[0]
		return page_id

	def get_links(self):
		text = self.data['query']['pages']['1808130']['revisions'][0]['*']
		lis = []
		index = text.find("\n*[[")
		while index != -1:
			rindex = text.find("]]", index)
			lis.append(self.base_url+text[index+4:rindex].replace(' ', "_"))
			index = text.find("\n*[[", rindex)
		return lis

	def print_data(self):
		print("Page id is : ", self.page_id)
		print("Reference Links : ", )
		for i in self.reference_links:
			print(i)

	def get_info(self):
		self.page_id = self.get_pageid()
		self.reference_links = self.get_links()
		self.print_data()
		return "Done"



def main():
	url = 'https://en.wikipedia.org/w/api.php?format=json&action=query&titles=SMALL&prop=revisions&rvprop=content'
	parser = JsonParser(url)
	parser.get_info()

if __name__ == '__main__':
	main()

