from ParkingLot import ParkingLot
from Location import Location
from ParkingSpot import ParkingSpot
class SingleLevel(ParkingLot):
	"""docstring for SingleLevel"""
	def __init__(self, location, parkingSpots, w, l, h):
		ParkingLot.__init__(self, location, parkingSpots, w, l, h)

	def Demension():
		return self.width * self*height

