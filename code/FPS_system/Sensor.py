
class Sensor():
	"""docstring for Sensor"""
	def __init__(self, arg):
		super(Sensor, self).__init__()
		self.arg = arg
	def __str__(self):
		return "This is a {}".format(str(self.__class__.__name__))
		