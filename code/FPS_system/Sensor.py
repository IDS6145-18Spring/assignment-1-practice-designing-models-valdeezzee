
class Sensor():
	"""docstring for Sensor"""
	def __init__(self):		
		self.objectDetected = False
		self.lifeSpan = 100.0

	def GetLifeSpan(self):
		return self.lifeSpan

	def GetObjectDetected(self):
		return self.objectDetected


	def __str__(self):
		return "This is a {}".format(str(self.__class__.__name__))
		