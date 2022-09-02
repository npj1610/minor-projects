import requests
import json
import time

class Cache:
	file = "mem.json"
	refresh_time = 3600

	def __init__(self):
		self.mem = {}
	
	def requestURL(self, url, cookies=None, requestWaitingTime=None):
		try:
			page = self.mem[url]
			if Cache.refresh_time < time.time() - page[0]:
				raise ValueError()
			return page[1]
		except (KeyError, ValueError):
			# only waits if a request is needed
			if requestWaitingTime is not None:
				time.sleep(requestWaitingTime)
			response = None
			if cookies is None:
				response = requests.get(url=url)
			else:
				response = requests.get(url=url, cookies=cookies)
			page = response.content.decode(response.encoding)
			self.mem[url] = (time.time(), page)
			return page

	def save(self):
		jmem = json.dumps(self.mem)
		with open(Cache.file, 'w') as f:
			f.write(str(jmem))

	def __exit__(self, exc_type, exc_value, tb):
		self.save()

	def load(self):
		try:
			with open(Cache.file, 'r') as f:
				self.mem = json.load(f)
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			pass
		
	def __enter__(self):
		self.load()
		return self