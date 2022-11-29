import json

class Config:
	def __init__(self, filename):
		self.filename = filename
		self.configs = json.loads(open(filename, "r").read())
	
	def write(self, type_, arg1, arg2=None):
		if type_ == "new server":
			self.configs["servers"][str(arg1)] = {}
		elif type_ == "modchannel":
			self.configs["servers"][str(arg2)]["mod_channel"] = arg1
	
	def send(self):
		json.dump(self.configs, open(self.filename, 'w'), indent=4)