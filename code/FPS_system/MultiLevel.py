from ParkingLot import ParkingLot
from Location import Location
from ParkingSpot import ParkingSpot
class MulitLevel(ParkingLot):
	"""docstring for MulitLevel"""
	def __init__(self, location, parkingSpots, w, l, h, f):
		self.floors = f
		ParkingLot.__init__(self, location, parkingSpots, w, l, h)

	def Dimensions(self):
		return self.width * self.length * self.height
