#The parent class include title and duration
class Video():
	def __init__(self, title, duration):
		print("Parent constructor called")
		self.title = title
		self.duration = duration
		