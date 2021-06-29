#!/usrr/bin/env python
import requests, re, urlparse

class Attachweb:
	
	def __init__(self, link, ignore):
		self.links_to_ignore = ignore
		self.session = requests.Session()
		self.saved_link = []
		self.start_link = link

	def write_in_file(self, url):
		with open("c:\Python27\url_test.txt", "a+") as text:
			text.writelines(url+"\n")

	def extract_links(self, url):
		try:
			result = self.session.get(url)
			page_content = result.content
			return re.findall('(?:href=")(.*?)"', page_content)

		except Exception:
			pass

	def run(self, target_url = None):
		if target_url == None:
			target_url = self.start_link
			
		url_links_in_page = self.extract_links(target_url)
		if url_links_in_page:
			for url in url_links_in_page:
				url = urlparse.urljoin(self.start_link, url)
				if "#" in url:
					url = url.split("#")[0] 
				if url not in self.saved_link and target_url in url and url not in links_to_ignore:
					self.saved_link.append(url)
					self.write_in_file(url)
					print(url)
					self.run(url)

	def extract_forms(self, url):
		response = self.session.get(target_url)
		parsed_html = BeautifulSoup(response.content)
		return parsed_html.findAll("form")

	def submit_form(self, form, value, url):
		action = form.get("action")
		post_url = urlparse.urljoin(url, action)
		method = form.get("method")
		inputs_list = form.findAll("input")
		post_data = {}
		for input in inputs_list:
			input_name = input.get("name")
			input_type = input.get("type")
			input_value = input.get("value")
			if input_type == "text":
				input_value = "test"

			post_data[input_name] = input_value
		if method == "post":	
			return self.session.post(post_url, data = post_data)
		return self.session.get(post_url, params = post_data)

	def testing(self):
		for link in saved_link:
			forms = self.extract_forms
			for form in forms:
				print("testing form in link : " + link)
			if "=" in link:
				print("link have form")
			
#target_url = raw_input("type_full_url")
#web = Attachweb(target_url)
#web.run(target_url)
