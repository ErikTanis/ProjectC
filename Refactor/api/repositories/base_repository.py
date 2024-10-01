class BaseRepository:
	def __init__(self, path, is_debug):
		self.path = path
		self.is_debug = is_debug

	def save(self, data):
		if self.is_debug:
			self.data = data
		else:
			file = open(self.path, "w")
			json.dump(data, file)
			file.close()

	def load(self):
		if self.is_debug:
			return self.data
		else:
			file = open(self.path, "r")
			data = json.load(file)
			file.close()
			return data