from Location import Location
from ParkingSpot import ParkingSpot

class ParkingLot():
	"""docstring for ParkingLot"""
	def __init__(self, location, parkingSpots, w, l, h):
		self.location = location
		self.parkingSpots = parkingSpots
		self.width = w
		self.length = l
		self.height = h

	def Dimensions(self):
		raise NotImplementError("Please Implement the Area method!")
		#Make sure the subclass defiens this method
		return None

	def GetParkingSpots(self):
		return self.parkingSpots

	def GetLocatoin(self):
		return self.location

	def __str__(self):
		return "This is a {} ParkingLot with {} parking spots available".format(str(self.__class__.__name__), len(self.parkingSpots))

