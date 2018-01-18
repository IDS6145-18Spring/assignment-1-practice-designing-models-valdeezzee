import random
from Sensor import Sensor
class ParkingSpot:

	def __init__(self, number, cost, sensor):
		self.spotNumber = number
		self.cost = cost
		self.sensor = sensor
		self.occupied = False
	
	def Area(self):
		raise NotImplementedError("Please Implement the Area method!")
		#Make sure the subclass defines this method
		return None

	def SpotNumber(self):		
		'''Returns the parking spot number'''
		return self.spotNumber

	def SetOccupied(self):
		self.occupied = self.sensor.GetObjectDetected()


	def __str__(self):
		price = ""
		if self.cost == 0.0:
			price = "free to park."
		else:
			price = str(self.cost) + " to park."
		return "Parking Spot is of type {} at Spot Number {} and it is {}".format(str(self.__class__.__name__),self.spotNumber, price)

