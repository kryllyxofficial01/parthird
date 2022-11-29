import json

class Config:
	def __init__(self, filename):
		self.filename = filename
		self.configs = json.loads(open(filename, "r").read())
	
	def write(self, type_, data):
		if type_ == "new server":
			self.configs["servers"][data] = {}
	
	def send(self):
		json.dump(self.configs, open(self.filename, 'w'), indent=4)