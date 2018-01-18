
class Sensor():
	"""docstring for Sensor"""
	def __init__(self):		
		self.objectDetected = False
		self.lifeSpan = 100.0
		self.timer = 0.0
		self.startTimer = false

	def GetLifeSpan(self):
		return self.lifeSpan

	def GetObjectDetected(self):
		return self.objectDetected

	def StartDestinationTimer(self, startTime):
		'''Starts a timer to check how long it will take to get to a spot'''
		self.startTimer = startTime
		while self.startTimer:
			self.time += 1

	def __str__(self):
		return "This is a {}".format(str(self.__class__.__name__))
		